/* 20210127, zjc, MILP */

/* 输入s盒所有的pattern，生成一个大的不等式集合，描述了这个s盒的行为
*但是直接把所有的这些不等式输给gurobi算不合理，因为存在大量冗余
* 这个算法就是去冗余，找出一个最优的不等式子集
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


int spilt_n(string s)//每行以‘，'来统计有多个子字符串
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
字符串分割方法
将str以分隔符',' 分割到 字符串数组 pStr，subStrCount为分割后字串个数
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
    //字符串不是以分隔符结束(最后一个分割符后还有字符串)
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
    //std::vector<std::vector<int>> vec(n,std::vector<int>(m,1)) //初始化为1 也可以为其他数
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
    //把数值形式的数0-255转化为一个点（bin数组形式）
    std::vector<int> point;
    for (int k = 0; k < 10; k++) {
        //point[k] = (num >> k) % 2;
        point.push_back((num >> k) % 2);
    }
    return point;
}

int point_to_int(std::vector<int> point_vec) {
    //把一个点（bin数组形式）转化为数值形式
    int translated_num = 0;
    int point_size = point_vec.size();
    for (int i = 0; i < point_size; i++) {
        translated_num += point_vec[i] * pow(2, i);
    }

    return translated_num;
}

bool is_point_satisfy_ineqVector(std::vector<int>& point_vec, std::vector<int>& set_vec) {
    //验证某个点是否满足不等式。
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

    //先遍历不等式集合，对每个不等式都设定一个参数，再遍历所有的非pattern,即集合B，如果有一个B中点不满足这个不等式，就把参数+1，两重循环
    vector<vector<int> >::iterator it1;//声明一个迭代器，来访问所有的不等式。 
    vector<int> weight_of_ineqs;
    for (it1 = ineq_vector.begin(); it1 != ineq_vector.end(); it1++)
    {
        int counter = 0;
        vector<vector<int> >::iterator it2;//声明一个迭代器，来访问B_vector容器
        for (it2 = B_vector.begin(); it2 != B_vector.end(); it2++) {
            if (false == is_point_satisfy_ineqVector(*it2, *it1)) {
                counter += 1;
            }
        }
        weight_of_ineqs.push_back(counter);

    }

    //找出最大权重的不等式，拷贝出来，把他加入到king_vector中。
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
    //把king写入到文件中，追加 
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



    //更新B_vector,方法，对于king不等式，重新遍历B，凭借点满足不等式与否对B做分类，最后swap

    vector<vector<int>> vec_swapwith_B_vector;//把这个不等式对应的maxmun_ineq_weight个点从B_vector中删除
    vector<vector<int> >::iterator it4;//声明一个迭代器，来访问B_vector容器，作用：遍历或者指向vector容器的元素 
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
            //把不等式，和对应的点打出来到文件中。
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
    //从不等式集合里面删除本轮的king_ineq, 这个不等式标记为0 0 0 0 0 0 0 0 0 ，这样集合B中的点都会满足，计数为0，在队伍末端
    //ineq_vector.at(maxmun_ineq_label).clear();
    //换一种方法更新B
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
    //首先，从文件中读取所有的不等式，记为一个容器big_set，元素为一维数组长度为9
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
    std::vector<std::vector<int>> big_set;  //用来存所有的不等式

    int mid = 0;

    while (!in.eof())
    {

        string temp;
        getline(in, temp);//这个temp里面是一个string，一行元素，形如3,-1,0,1,-1,-1,0,1,-1   需要把他们按，分开，放到一个数组中，再放入到容器big_set中
        string* pStr;  //未释放
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
    //检查big_set
    for (int i = 0; i < big_set.size(); i++)//输出二维动态数组
    {
        for (int j = 0; j < big_set[i].size(); j++)
        {
            cout << big_set[i][j] << " ";
        }
        cout << "\n";
    }
    */


    //从文件中读取所有的patterns，放在容器中vector_A中，元素为一维数组
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
        getline(in, temp);//这个temp里面是一个string，一行元素，形如3,-1,0,1,-1,-1,0,1,-1   需要把他们按，分开，放到一个数组中，再放入到容器big_set中
        string* pStr = NULL;  //未释放
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
    //对应生成所有的非patterns，放在容器vector_B中，元素为一组数组，并保存为文件
    int num_of_init = 1024;
    std::vector<std::vector<int>> vector_Init_128;
    for (int i = 0; i < num_of_init; i++) {
        std::vector<int> temp_vec3;
        for (int j = 0; j < num_of_size; j++) {
            //把i转化为8位的二进制，分别对vector_Init_512[i][j]的每一位赋值，先化为二进制的string就可以了
            //vector_Init_512[i][j] = (i >> j) % 2;
            temp_vec3.push_back((i >> j) % 2);
        }
        vector_Init_128.push_back(temp_vec3);
    }
    //把A中的点全化为十进制，存在一个数组里面，遍历0-255，生成A的补集vector_B      所以问题出在B上面
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
        //如果find_label 没找到，就是说这个下标在B中，把他转化为二进制加入到B_vector中即可
        if (find_label == false) {
            vector<int> temp_member_B;
            for (int k = num_of_size - 1; k >= 0; k--) {
                //temp_member_B[k] = (i >> k) % 2;
                temp_member_B.push_back((i >> k) % 2);
            }
            vector_B.push_back(temp_member_B);
        }
    }

    //备份vector_B至vector_B_bak
    std::vector<std::vector<int>> vector_B_bak = vector_B;
    //把非patterns全写入文件中
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
    //执行步骤3，进行循环，跳出条件为 temp_vector_B 为空

    while (0 != vector_B.size()) {
        finda_king_ineq(big_set, vector_B, greddy_king_subset);
        //if (vector_B.size() == 43) {
        //    break;
        //}
    }


    //把greddy_king_subset打印并写入到文件中保存

    //释放资源
    bool check1 = check_patterns_all_pass_king_ineq_set(vector_A, greddy_king_subset);
    bool check2 = check_not_patterns_exist_cantpass_king_ineq_set(vector_B_bak, greddy_king_subset);
    cout << check1 << endl;
    cout << check2 << endl;

    //测试伟哲的不等式的结果
    //A_vector有了，就只要把他的文件导出来


    in.open("new_ineq_wz.txt", ios::in);
    if (!in) {
        cout << "open file fail!";
    }
    else cout << "open file success!" << endl;
    std::vector<std::vector<int>> ineq_set_wz;  //用来存所有的不等式

    int mid_wz = 0;

    while (!in.eof())
    {

        string temp;
        getline(in, temp);//这个temp里面是一个string，一行元素，形如3,-1,0,1,-1,-1,0,1,-1   需要把他们按，分开，放到一个数组中，再放入到容器big_set中
        string* pStr;  //未释放
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
