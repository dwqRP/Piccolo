/* 20210127, zjc, MILP */

/* ����s�����е�pattern������һ����Ĳ���ʽ���ϣ����������s�е���Ϊ
*����ֱ�Ӱ����е���Щ����ʽ���gurobi�㲻������Ϊ���ڴ�������
* ����㷨����ȥ���࣬�ҳ�һ�����ŵĲ���ʽ�Ӽ�
*/

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#define PATTERNSSIZE 33
using namespace std;

int spilt_n(string s);
bool is_point_satisfy_ineqVector(std::vector<int>& point_vec, std::vector<int>& set_vec);
int point_to_int(std::vector<std::vector<int> > point_vec);
std::vector<int> int_to_point(int num);
void finda_king_ineq(std::vector<std::vector<int> >& ineq_vector, std::vector<std::vector<int> >& B_vector, std::vector<std::vector<int> >& king_vector);
bool check_patterns_all_pass_king_ineq_set(std::vector<std::vector<int> >& patterns_vector, std::vector<std::vector<int> >& king_ineq_set_vector);
bool check_not_patterns_exist_cantpass_king_ineq_set(std::vector<std::vector<int> >& not_patterns_vector, std::vector<std::vector<int> >& king_ineq_set_vector);


int spilt_n(string s)//ÿ���ԡ���'��ͳ���ж�����ַ���
{
    const char* ch;
    unsigned int i, count = 1;
    ch = s.c_str();
    for (i = 0; i < s.length() - 1; i++)
    {
        if (ch[i] == ',')count++;
    }
    //    cout<<"count:"<<count<<endl;
    return count;
}

int s2i(const char* str, int* num)
{
    int i = 0;
    *num = 0;
    if (strlen(str) == 0) {
        return -1;
    }
    if (*(str) != '-') {
        for (i = 0; i < strlen(str); i++) {
            if (*(str + i) < '0' || *(str + i) > '9') {
                return -1;
            }
            *num = (*num) * 10 + (*(str + i)) - '0';
        }
    }
    else {
        for (i = 1; i < strlen(str); i++)
        {

            if (*(str + i) < '0' || *(str + i) > '9')
            {
                return -1;
            }
            *num = (*num) * 10 + (*(str + i)) - '0';
        }
        *num = (*num) * -1;
    }

    return 0;
}

/*
�ַ����ָ��
��str�Էָ���',' �ָ �ַ������� pStr��subStrCountΪ�ָ���ִ�����
*/

int splitString(string str, string** pStr, int* subStrCount)
{
    int strLen = str.length();
    int pLen = (strLen + 4) / 4 * 4;
    char* pSource = new char[pLen];
    char* p;
    memset(pSource, 0, pLen);
    memcpy(pSource, str.c_str(), str.length());
    (*subStrCount) = 0;
    for (int i = 0; i < strLen; i++)
    {
        if (*(pSource + i) == ',')
        {
            (*subStrCount)++;
            *(pSource + i) = 0;
        }
    }
    //�ַ��������Էָ�������(���һ���ָ�������ַ���)
    if (*(pSource + strLen - 1) != ',')
    {
        (*subStrCount)++;
    }
    *pStr = new string[*(subStrCount)];
    p = pSource;
    for (int i = 0; i < *subStrCount; i++)
    {
        (*pStr)[i] = p;
        p += (*pStr)[i].length() + 1;
    }
    return 0;
}

int test(void)
{
    int n = 3;
    int m = 4;
    std::vector<std::vector<int>> vec(n, std::vector<int>(m));
    //std::vector<std::vector<int>> vec(n,std::vector<int>(m,1)) //��ʼ��Ϊ1 Ҳ����Ϊ������
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            vec[i][j] = i + j;
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            std::cout << vec[i][j];
        std::cout << std::endl;
    }
    return 0;
}


std::vector<int> int_to_point(int num) {
    //����ֵ��ʽ����0-255ת��Ϊһ���㣨bin������ʽ��
    std::vector<int> point;
    for (int k = 0; k < 10; k++) {
        //point[k] = (num >> k) % 2;
        point.push_back((num >> k) % 2);
    }
    return point;
}

int point_to_int(std::vector<int> point_vec) {
    //��һ���㣨bin������ʽ��ת��Ϊ��ֵ��ʽ
    int translated_num = 0;
    int point_size = point_vec.size();
    for (int i = 0; i < point_size; i++) {
        translated_num += point_vec[i] * pow(2, i);
    }

    return translated_num;
}

bool is_point_satisfy_ineqVector(std::vector<int>& point_vec, std::vector<int>& set_vec) {
    //��֤ĳ�����Ƿ����㲻��ʽ��
    bool label_satisfy = true;
    int sum = 0;
    if (point_vec.size() == 10 && set_vec.size() == 11) {
        for (int i = 0; i < 10; i++) {
            int j = i + 1;
            sum += point_vec[i] * set_vec[j];
        }
        sum += set_vec[0];
        if (sum >= 0) {
            label_satisfy = true;
        }
        else {
            label_satisfy = false;
        }

    }
    else {
        cout << "allert, input fault!" << endl;
    }
    return label_satisfy;
}

void finda_king_ineq(std::vector<std::vector<int> >& ineq_vector, std::vector<std::vector<int> >& B_vector, std::vector<std::vector<int> >& king_vector) {

    int size_of_B_vector = 0;
    int size_of_ineq_vector = 0;
    size_of_B_vector = B_vector.size();
    size_of_ineq_vector = ineq_vector.size();

    //�ȱ�������ʽ���ϣ���ÿ������ʽ���趨һ���������ٱ������еķ�pattern,������B�������һ��B�е㲻�����������ʽ���ͰѲ���+1������ѭ��
    vector<vector<int> >::iterator it1;//����һ�������������������еĲ���ʽ�� 
    vector<int> weight_of_ineqs;
    for (it1 = ineq_vector.begin(); it1 != ineq_vector.end(); it1++)
    {
        int counter = 0;
        vector<vector<int> >::iterator it2;//����һ����������������B_vector����
        for (it2 = B_vector.begin(); it2 != B_vector.end(); it2++) {
            if (false == is_point_satisfy_ineqVector(*it2, *it1)) {
                counter += 1;
            }
        }
        weight_of_ineqs.push_back(counter);

    }

    //�ҳ����Ȩ�صĲ���ʽ�������������������뵽king_vector�С�
    int maxmun_ineq_label = 0;
    int maxmun_ineq_weight = 0;
    maxmun_ineq_weight = weight_of_ineqs[maxmun_ineq_label];
    for (int i = 1; i < weight_of_ineqs.size(); i++) {
        if (weight_of_ineqs[i] >= maxmun_ineq_weight) {
            maxmun_ineq_label = i;
            maxmun_ineq_weight = weight_of_ineqs[maxmun_ineq_label];
        }
    }



    vector<int> king_ineq;
    vector<int>::iterator it3;
    for (it3 = ineq_vector.at(maxmun_ineq_label).begin(); it3 < ineq_vector.at(maxmun_ineq_label).end(); it3++) {
        king_ineq.push_back(*it3);
    }
    king_vector.push_back(king_ineq);
    //��kingд�뵽�ļ��У�׷�� 
    ofstream outfile;
    outfile.open("king_ineq_file.txt", ios::app);
    if (!outfile) {
        cout << "creat file fail!";
    }
    else cout << "open file for write success!" << endl;

    for (it3 = king_ineq.begin(); it3 < king_ineq.end(); it3++) {
        outfile << *it3 << ',';
    }
    outfile << endl;
    outfile.close();



    //����B_vector,����������king����ʽ�����±���B��ƾ������㲻��ʽ����B�����࣬���swap

    vector<vector<int>> vec_swapwith_B_vector;//���������ʽ��Ӧ��maxmun_ineq_weight�����B_vector��ɾ��
    vector<vector<int> >::iterator it4;//����һ����������������B_vector���������ã���������ָ��vector������Ԫ�� 
    ofstream outfile3;
    outfile3.open("king_ineq_check_with_B_point.txt", ios::app);
    if (!outfile3) {
        cout << "creat file fail!";
    }
    else cout << "open file for write success!" << endl;
    vector<int>::iterator it5;
    outfile3 << "====================================================" << endl << "the inequality:[";
    for (it5 = ineq_vector.at(maxmun_ineq_label).begin(); it5 < ineq_vector.at(maxmun_ineq_label).end(); it5++) {
        outfile3 << *it5 << ',';
    }
    outfile3 << "],cut off impossible point are:" << endl;
    for (it4 = B_vector.begin(); it4 != B_vector.end(); it4++) {
        if (false == is_point_satisfy_ineqVector(*it4, ineq_vector.at(maxmun_ineq_label))) {
            //�Ѳ���ʽ���Ͷ�Ӧ�ĵ��������ļ��С�
            vector<int>::iterator it6;
            for (it6 = (*it4).begin(); it6 < (*it4).end(); it6++) {
                outfile3 << *it6 << ',';
            }
            outfile3 << endl;

        }
        else
        {
            vec_swapwith_B_vector.push_back(*(it4));
        }
    }
    outfile3.close();

    B_vector.swap(vec_swapwith_B_vector);
    //�Ӳ���ʽ��������ɾ�����ֵ�king_ineq, �������ʽ���Ϊ0 0 0 0 0 0 0 0 0 ����������B�еĵ㶼�����㣬����Ϊ0���ڶ���ĩ��
    //ineq_vector.at(maxmun_ineq_label).clear();
    //��һ�ַ�������B
    ineq_vector.erase(ineq_vector.begin() + maxmun_ineq_label);

    if (maxmun_ineq_weight == 0 && size_of_B_vector != 0) {
        //exit(1);
        //cout << size_of_B_vector << endl;
    }
}


bool check_patterns_all_pass_king_ineq_set(std::vector<std::vector<int> >& patterns_vector, std::vector<std::vector<int> >& king_ineq_set_vector) {
    bool check_label = true;
    vector<vector<int>>::iterator it7;
    vector<vector<int>>::iterator it8;
    for (it7 = patterns_vector.begin(); it7 < patterns_vector.end(); it7++) {

        for (it8 = king_ineq_set_vector.begin(); it8 < king_ineq_set_vector.end(); it8++) {
            if (false == is_point_satisfy_ineqVector(*it7, *it8)) {
                check_label = false;
            }
        }
    }
    if (true == check_label) {
        return true;
    }
    else {
        return false;
    }
}
bool check_not_patterns_exist_cantpass_king_ineq_set(std::vector<std::vector<int> >& not_patterns_vector, std::vector<std::vector<int> >& king_ineq_set_vector) {
    bool check_label = true;
    vector<vector<int>>::iterator it7;
    vector<vector<int>>::iterator it8;
    for (it7 = not_patterns_vector.begin(); it7 < not_patterns_vector.end(); it7++) {

        for (it8 = king_ineq_set_vector.begin(); it8 < king_ineq_set_vector.end(); it8++) {
            if (false == is_point_satisfy_ineqVector(*it7, *it8)) {
                check_label = false;
            }
        }
    }
    if (false == check_label) {
        return true;
    }
    else {
        return false;
    }
}

int main(int argc, char* argv[])
{
    //���ȣ����ļ��ж�ȡ���еĲ���ʽ����Ϊһ������big_set��Ԫ��Ϊһά���鳤��Ϊ9
    ifstream in;
    ofstream out;
    out.open("king_ineq_file.txt", ios::trunc);
    out.close();
    out.open("fish_point_B_vector_file.txt", ios::trunc);
    out.close();
    out.open("king_ineq_check_with_B_point.txt", ios::trunc);
    out.close();
    out.open("not_patterns_file.txt", ios::trunc);
    out.close();

    in.open("bigineq_file.txt", ios::in);
    if (!in) {
        cout << "open file fail!";
    }
    else cout << "open file success!" << endl;

    //vector<vector<int>>big_set;
    //int n = 327;
    //int m = 9;
    std::vector<std::vector<int>> big_set;  //���������еĲ���ʽ

    int mid = 0;

    while (!in.eof())
    {

        string temp;
        getline(in, temp);//���temp������һ��string��һ��Ԫ�أ�����3,-1,0,1,-1,-1,0,1,-1   ��Ҫ�����ǰ����ֿ����ŵ�һ�������У��ٷ��뵽����big_set��
        string* pStr;  //δ�ͷ�
        int* numbs;
        int subStrCount;
        int k = 0;
        splitString(temp, &pStr, &subStrCount);
        if (subStrCount <= 0)
        {
            return -1;
        }
        numbs = new int[subStrCount];
        for (int i = 0; i < subStrCount; i++)
        {
            s2i(pStr[i].c_str(), (numbs + i));
        }
        std::vector<int> temp_vec1;
        for (int i = 0; i < subStrCount; i++)
        {
            //cout << *(numbs + i) << " ";
            //big_set[mid][i] = *(numbs + i);
            //numbs[k] = *(numbs + i);
            temp_vec1.push_back(*(numbs + i));

        }
        big_set.push_back(temp_vec1);
        mid++;

    }
    in.close();
    /*
    //���big_set
    for (int i = 0; i < big_set.size(); i++)//�����ά��̬����
    {
        for (int j = 0; j < big_set[i].size(); j++)
        {
            cout << big_set[i][j] << " ";
        }
        cout << "\n";
    }
    */


    //���ļ��ж�ȡ���е�patterns������������vector_A�У�Ԫ��Ϊһά����
    //ifstream in;

    in.open("patterns_file.txt", ios::in);
    if (!in) {
        cout << "open file fail!";
    }
    else cout << "open file success!" << endl;
    //vector<vector<int>>big_set;
    int num_of_patterns = 33;
    int num_of_size = 10;
    std::vector<std::vector<int>> vector_A;

    int mid_2 = 0;
    while (!in.eof())
    {

        string temp;
        getline(in, temp);//���temp������һ��string��һ��Ԫ�أ�����3,-1,0,1,-1,-1,0,1,-1   ��Ҫ�����ǰ����ֿ����ŵ�һ�������У��ٷ��뵽����big_set��
        string* pStr = NULL;  //δ�ͷ�
        int* numbs = NULL;
        int subStrCount;
        int k = 0;
        splitString(temp, &pStr, &subStrCount);
        if (subStrCount <= 0)
        {
            return -1;
        }
        numbs = new int[subStrCount];
        for (int i = 0; i < subStrCount; i++)
        {
            s2i(pStr[i].c_str(), (numbs + i));
        }
        std::vector<int> temp_vec2;
        for (int i = 0; i < subStrCount; i++)
        {
            //cout << *(numbs + i) << " ";
            //vector_A[mid_2][i] = *(numbs + i);
            //numbs[k] = *(numbs + i);
            temp_vec2.push_back(*(numbs + i));

        }
        vector_A.push_back(temp_vec2);
        mid_2++;

    }
    in.close();
    //��Ӧ�������еķ�patterns����������vector_B�У�Ԫ��Ϊһ�����飬������Ϊ�ļ�
    int num_of_init = 1024;
    std::vector<std::vector<int>> vector_Init_128;
    for (int i = 0; i < num_of_init; i++) {
        std::vector<int> temp_vec3;
        for (int j = 0; j < num_of_size; j++) {
            //��iת��Ϊ8λ�Ķ����ƣ��ֱ��vector_Init_512[i][j]��ÿһλ��ֵ���Ȼ�Ϊ�����Ƶ�string�Ϳ�����
            //vector_Init_512[i][j] = (i >> j) % 2;
            temp_vec3.push_back((i >> j) % 2);
        }
        vector_Init_128.push_back(temp_vec3);
    }
    //��A�еĵ�ȫ��Ϊʮ���ƣ�����һ���������棬����0-255������A�Ĳ���vector_B      �����������B����
    //int num_of_vB = num_of_init - num_of_patterns;
    std::vector<std::vector<int>> vector_B;

    int A_Int_array[PATTERNSSIZE];
    for (int i = 0; i < PATTERNSSIZE; i++) {
        int temp_int_num = 0;
        for (int j = 0; j < 10; j++) {
            int k = 9 - j;
            temp_int_num += vector_A[i][j] * pow(2, k);
        }
        A_Int_array[i] = temp_int_num;
    }

    for (int i = 0; i < num_of_init; i++) {
        bool find_label = false;
        for (int j = 0; j < PATTERNSSIZE; j++) {
            if (i == A_Int_array[j]) {
                find_label = true;
            }
        }
        //���find_label û�ҵ�������˵����±���B�У�����ת��Ϊ�����Ƽ��뵽B_vector�м���
        if (find_label == false) {
            vector<int> temp_member_B;
            for (int k = num_of_size - 1; k >= 0; k--) {
                //temp_member_B[k] = (i >> k) % 2;
                temp_member_B.push_back((i >> k) % 2);
            }
            vector_B.push_back(temp_member_B);
        }
    }

    //����vector_B��vector_B_bak
    std::vector<std::vector<int>> vector_B_bak = vector_B;
    //�ѷ�patternsȫд���ļ���
    ofstream outfile;
    outfile.open("not_patterns_file.txt", ios::app);
    if (!outfile) {
        cout << "creat file fail!";
    }
    else cout << "open file for write success!" << endl;
    vector<vector<int> >::iterator it9;
    for (it9 = vector_B.begin(); it9 != vector_B.end(); it9++) {
        vector<int>::iterator it6;
        for (it6 = (*it9).begin(); it6 < (*it9).end(); it6++) {
            outfile << *it6 << ',';
        }
        outfile << endl;
    }
    outfile << endl;
    outfile.close();



    std::vector<std::vector<int>> greddy_king_subset;
    //ִ�в���3������ѭ������������Ϊ temp_vector_B Ϊ��

    while (0 != vector_B.size()) {
        finda_king_ineq(big_set, vector_B, greddy_king_subset);
        //if (vector_B.size() == 43) {
        //    break;
        //}
    }


    //��greddy_king_subset��ӡ��д�뵽�ļ��б���

    //�ͷ���Դ
    bool check1 = check_patterns_all_pass_king_ineq_set(vector_A, greddy_king_subset);
    bool check2 = check_not_patterns_exist_cantpass_king_ineq_set(vector_B_bak, greddy_king_subset);
    cout << check1 << endl;
    cout << check2 << endl;

    //����ΰ�ܵĲ���ʽ�Ľ��
    //A_vector���ˣ���ֻҪ�������ļ�������


    in.open("new_ineq_wz.txt", ios::in);
    if (!in) {
        cout << "open file fail!";
    }
    else cout << "open file success!" << endl;
    std::vector<std::vector<int>> ineq_set_wz;  //���������еĲ���ʽ

    int mid_wz = 0;

    while (!in.eof())
    {

        string temp;
        getline(in, temp);//���temp������һ��string��һ��Ԫ�أ�����3,-1,0,1,-1,-1,0,1,-1   ��Ҫ�����ǰ����ֿ����ŵ�һ�������У��ٷ��뵽����big_set��
        string* pStr;  //δ�ͷ�
        int* numbs;
        int subStrCount;
        int k = 0;
        splitString(temp, &pStr, &subStrCount);
        if (subStrCount <= 0)
        {
            return -1;
        }
        numbs = new int[subStrCount];
        for (int i = 0; i < subStrCount; i++)
        {
            s2i(pStr[i].c_str(), (numbs + i));
        }
        std::vector<int> temp_vec1;
        for (int i = 0; i < subStrCount; i++)
        {
            //cout << *(numbs + i) << " ";
            //big_set[mid][i] = *(numbs + i);
            //numbs[k] = *(numbs + i);
            temp_vec1.push_back(*(numbs + i));

        }
        ineq_set_wz.push_back(temp_vec1);
        mid++;

    }
    in.close();
    bool check3 = check_patterns_all_pass_king_ineq_set(vector_A, ineq_set_wz);
    bool check4 = check_not_patterns_exist_cantpass_king_ineq_set(vector_B_bak, ineq_set_wz);
    cout << check3 << endl;
    cout << check4 << endl;
    return 0;
}
