#include <iostream>
using namespace std;

int main() {
	int cnt = 0;
	for (int a0 = 0; a0 < 2; a0++) {
		for (int a1 = 0; a1 < 2; a1++) {
			for (int b0 = 0; b0 < 2; b0++) {
				for (int b1 = 0; b1 < 2; b1++) {
					for (int c0 = 0; c0 < 2; c0++) {
						for (int c1 = 0; c1 < 2; c1++) {
							for (int d0 = 0; d0 < 2; d0++) {
								for (int d1 = 0; d1 < 2; d1++) {
									for (int e0 = 0; e0 < 2; e0++) {
										for (int e1 = 0; e1 < 2; e1++) {
											
											int flag1 = (b1 - b0 + d0 - d1 + e1 - e0 >= 0) ? 1 : 0;
											int flag2 = (a1 - a0 + c1 - c0 + e0 - e1 >= 0) ? 1 : 0;
											int flag3 = (b0 - d0 + e1 - e0 >= 0) ? 1 : 0;
											int flag4 = (b1 - b0 + e0 - d0 >= 0) ? 1 : 0;
											int flag5 = (1 - b1 + d1 - e1 >= 0) ? 1 : 0;
											int flag6 = (a0 + c1 - c0 - e0 >= 0) ? 1 : 0;
											int flag7 = (a1 - a0 + c0 - e0 >= 0) ? 1 : 0;
											int flag8 = (1 - a1 - c1 + e1 >= 0) ? 1 : 0;
											int flag9 = (b1 - d1 >= 0) ? 1 : 0;
											int flag10 = (e1 - d1 >= 0) ? 1 : 0;
											int flag11 = (a1 - e1 >= 0) ? 1 : 0;
											int flag12 = (c1 - e1 >= 0) ? 1 : 0;

										

											if (flag1 && flag2 && flag3 && flag4 && flag5 && flag6 && flag7 && flag8 && flag9 && flag10 && flag11 && flag12) {
												cnt++;
												cout << a0 << a1 << ' ' << b0 << b1 << ' ' << c0 << c1 << ' ' << d0 << d1 << ' ' << e0 << e1 << endl;
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	cout << cnt;
}