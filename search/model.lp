\ Model Piccolo
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  3 Sprobx0[0] + 3 Sprobx0[1] + 3 Sprobx0[2] + 3 Sprobx0[3] + 3 Sprobx0[4]
   + 3 Sprobx0[5] + 3 Sprobx0[6] + 3 Sprobx0[7] + 3 Sprobx0[8]
   + 3 Sprobx0[9] + 3 Sprobx0[10] + 3 Sprobx0[11] + 3 Sprobx0[12]
   + 3 Sprobx0[13] + 3 Sprobx0[14] + 3 Sprobx0[15] + 2 Sproby0[0]
   + 2 Sproby0[1] + 2 Sproby0[2] + 2 Sproby0[3] + 2 Sproby0[4]
   + 2 Sproby0[5] + 2 Sproby0[6] + 2 Sproby0[7] + 2 Sproby0[8]
   + 2 Sproby0[9] + 2 Sproby0[10] + 2 Sproby0[11] + 2 Sproby0[12]
   + 2 Sproby0[13] + 2 Sproby0[14] + 2 Sproby0[15] + 3 Sprobx1[0]
   + 3 Sprobx1[1] + 3 Sprobx1[2] + 3 Sprobx1[3] + 3 Sprobx1[4]
   + 3 Sprobx1[5] + 3 Sprobx1[6] + 3 Sprobx1[7] + 3 Sprobx1[8]
   + 3 Sprobx1[9] + 3 Sprobx1[10] + 3 Sprobx1[11] + 3 Sprobx1[12]
   + 3 Sprobx1[13] + 3 Sprobx1[14] + 3 Sprobx1[15] + 2 Sproby1[0]
   + 2 Sproby1[1] + 2 Sproby1[2] + 2 Sproby1[3] + 2 Sproby1[4]
   + 2 Sproby1[5] + 2 Sproby1[6] + 2 Sproby1[7] + 2 Sproby1[8]
   + 2 Sproby1[9] + 2 Sproby1[10] + 2 Sproby1[11] + 2 Sproby1[12]
   + 2 Sproby1[13] + 2 Sproby1[14] + 2 Sproby1[15] + 3 Sprobx2[0]
   + 3 Sprobx2[1] + 3 Sprobx2[2] + 3 Sprobx2[3] + 3 Sprobx2[4]
   + 3 Sprobx2[5] + 3 Sprobx2[6] + 3 Sprobx2[7] + 3 Sprobx2[8]
   + 3 Sprobx2[9] + 3 Sprobx2[10] + 3 Sprobx2[11] + 3 Sprobx2[12]
   + 3 Sprobx2[13] + 3 Sprobx2[14] + 3 Sprobx2[15] + 2 Sproby2[0]
   + 2 Sproby2[1] + 2 Sproby2[2] + 2 Sproby2[3] + 2 Sproby2[4]
   + 2 Sproby2[5] + 2 Sproby2[6] + 2 Sproby2[7] + 2 Sproby2[8]
   + 2 Sproby2[9] + 2 Sproby2[10] + 2 Sproby2[11] + 2 Sproby2[12]
   + 2 Sproby2[13] + 2 Sproby2[14] + 2 Sproby2[15]
Subject To
 R118014: state0[0] + state0[1] + state0[2] + state0[3] + state0[4]
   + state0[5] + state0[6] + state0[7] + state0[8] + state0[9] + state0[10]
   + state0[11] + state0[12] + state0[13] + state0[14] + state0[15]
   + state0[16] + state0[17] + state0[18] + state0[19] + state0[20]
   + state0[21] + state0[22] + state0[23] + state0[24] + state0[25]
   + state0[26] + state0[27] + state0[28] + state0[29] + state0[30]
   + state0[31] + state0[32] + state0[33] + state0[34] + state0[35]
   + state0[36] + state0[37] + state0[38] + state0[39] + state0[40]
   + state0[41] + state0[42] + state0[43] + state0[44] + state0[45]
   + state0[46] + state0[47] + state0[48] + state0[49] + state0[50]
   + state0[51] + state0[52] + state0[53] + state0[54] + state0[55]
   + state0[56] + state0[57] + state0[58] + state0[59] + state0[60]
   + state0[61] + state0[62] + state0[63] >= 1
 R118015: - Sprobx0[0] - Sproby0[0] >= -1
 R118016: - state0[1] - state0[2] - state0[3] - beforeM0[1] + beforeM0[2]
   - beforeM0[3] + 4 Sprobx0[0] + 3 Sproby0[0] >= 0
 R118017: - 3 state0[0] - state0[2] + state0[3] - 3 beforeM0[0]
   - beforeM0[1] - 2 beforeM0[2] - 2 beforeM0[3] + 11 Sprobx0[0]
   + 7 Sproby0[0] >= 0
 R118018: - state0[1] - state0[2] - state0[3] - beforeM0[0] - 2 beforeM0[1]
   - beforeM0[2] - beforeM0[3] + 8 Sprobx0[0] + 4 Sproby0[0] >= 0
 R118019: - 2 state0[0] + state0[1] - 2 state0[3] - beforeM0[0]
   + 2 beforeM0[1] - beforeM0[3] + 4 Sprobx0[0] + 5 Sproby0[0] >= 0
 R118020: state0[0] - state0[1] + state0[3] - beforeM0[0] + beforeM0[1]
   + 2 beforeM0[2] - beforeM0[3] + 2 Sprobx0[0] + Sproby0[0] >= 0
 R118021: state0[0] - state0[1] - state0[3] + beforeM0[1] + beforeM0[3]
   + Sprobx0[0] + 2 Sproby0[0] >= 0
 R118022: state0[2] + beforeM0[1] - Sprobx0[0] >= 0
 R118023: - 3 state0[1] + 2 beforeM0[0] - beforeM0[1] + beforeM0[2]
   - beforeM0[3] + 4 Sprobx0[0] + 2 Sproby0[0] >= 0
 R118024: state0[1] + 2 beforeM0[0] + beforeM0[1] + beforeM0[3]
   - 2 Sprobx0[0] - Sproby0[0] >= 0
 R118025: - state0[0] - state0[1] + 2 state0[2] + beforeM0[0]
   + 2 beforeM0[2] + Sproby0[0] >= 0
 R118026: 2 state0[0] - 2 state0[1] - 2 state0[2] - 3 state0[3]
   - beforeM0[1] + beforeM0[2] - beforeM0[3] + 8 Sprobx0[0] + 4 Sproby0[0]
   >= 0
 R118027: - 3 state0[0] + state0[1] - state0[2] + state0[3] - 4 beforeM0[0]
   - beforeM0[1] - 2 beforeM0[2] - 2 beforeM0[3] + 12 Sprobx0[0]
   + 7 Sproby0[0] >= 0
 R118028: state0[0] + 2 state0[2] - beforeM0[0] - 3 beforeM0[1]
   - beforeM0[2] + 4 Sprobx0[0] + 2 Sproby0[0] >= 0
 R118029: state0[1] + beforeM0[0] - Sprobx0[0] >= 0
 R118030: 2 state0[0] + state0[1] + 2 state0[3] - beforeM0[0] - beforeM0[2]
   - beforeM0[3] + Sprobx0[0] + 2 Sproby0[0] >= 0
 R118031: state0[0] + state0[1] + state0[2] - Sprobx0[0] >= 0
 R118032: - state0[0] - state0[1] + state0[3] - beforeM0[0] - 2 beforeM0[1]
   + beforeM0[2] + beforeM0[3] + 4 Sprobx0[0] + 3 Sproby0[0] >= 0
 R118033: state0[1] - state0[2] + state0[3] + beforeM0[0] - beforeM0[1]
   - beforeM0[2] + beforeM0[3] + Sprobx0[0] + 3 Sproby0[0] >= 0
 R118034: state0[0] - state0[1] - 2 state0[2] - state0[3] + beforeM0[0]
   - 2 beforeM0[2] + 2 beforeM0[3] + 4 Sprobx0[0] + 4 Sproby0[0] >= 0
 R118035: - state0[0] + state0[1] - state0[2] + state0[3] - 4 beforeM0[0]
   - beforeM0[1] - beforeM0[3] + 7 Sprobx0[0] + 4 Sproby0[0] >= 0
 R118036: - 3 state0[0] - state0[1] - state0[2] - 2 state0[3]
   - 3 beforeM0[0] - 2 beforeM0[1] - beforeM0[2] + 2 beforeM0[3]
   + 12 Sprobx0[0] + 7 Sproby0[0] >= 0
 R118037: state0[1] + state0[2] + beforeM0[0] + beforeM0[1] - 2 Sprobx0[0]
   - Sproby0[0] >= 0
 R118038: state0[0] - 3 state0[1] - 4 state0[2] - 2 state0[3] - beforeM0[1]
   + 3 beforeM0[2] + 3 beforeM0[3] + 10 Sprobx0[0] + 2 Sproby0[0] >= 0
 R118039: 2 state0[0] + 2 state0[1] - state0[2] + 4 state0[3]
   - 5 beforeM0[0] - beforeM0[1] + beforeM0[2] + beforeM0[3] + 4 Sprobx0[0]
   + Sproby0[0] >= 0
 R118040: - state0[0] - state0[1] - 3 state0[2] + state0[3] + 2 beforeM0[1]
   + beforeM0[3] + 4 Sprobx0[0] + 2 Sproby0[0] >= 0
 R118041: - Sprobx0[1] - Sproby0[1] >= -1
 R118042: - state0[5] - state0[6] - state0[7] - beforeM0[5] + beforeM0[6]
   - beforeM0[7] + 4 Sprobx0[1] + 3 Sproby0[1] >= 0
 R118043: - 3 state0[4] - state0[6] + state0[7] - 3 beforeM0[4]
   - beforeM0[5] - 2 beforeM0[6] - 2 beforeM0[7] + 11 Sprobx0[1]
   + 7 Sproby0[1] >= 0
 R118044: - state0[5] - state0[6] - state0[7] - beforeM0[4] - 2 beforeM0[5]
   - beforeM0[6] - beforeM0[7] + 8 Sprobx0[1] + 4 Sproby0[1] >= 0
 R118045: - 2 state0[4] + state0[5] - 2 state0[7] - beforeM0[4]
   + 2 beforeM0[5] - beforeM0[7] + 4 Sprobx0[1] + 5 Sproby0[1] >= 0
 R118046: state0[4] - state0[5] + state0[7] - beforeM0[4] + beforeM0[5]
   + 2 beforeM0[6] - beforeM0[7] + 2 Sprobx0[1] + Sproby0[1] >= 0
 R118047: state0[4] - state0[5] - state0[7] + beforeM0[5] + beforeM0[7]
   + Sprobx0[1] + 2 Sproby0[1] >= 0
 R118048: state0[6] + beforeM0[5] - Sprobx0[1] >= 0
 R118049: - 3 state0[5] + 2 beforeM0[4] - beforeM0[5] + beforeM0[6]
   - beforeM0[7] + 4 Sprobx0[1] + 2 Sproby0[1] >= 0
 R118050: state0[5] + 2 beforeM0[4] + beforeM0[5] + beforeM0[7]
   - 2 Sprobx0[1] - Sproby0[1] >= 0
 R118051: - state0[4] - state0[5] + 2 state0[6] + beforeM0[4]
   + 2 beforeM0[6] + Sproby0[1] >= 0
 R118052: 2 state0[4] - 2 state0[5] - 2 state0[6] - 3 state0[7]
   - beforeM0[5] + beforeM0[6] - beforeM0[7] + 8 Sprobx0[1] + 4 Sproby0[1]
   >= 0
 R118053: - 3 state0[4] + state0[5] - state0[6] + state0[7] - 4 beforeM0[4]
   - beforeM0[5] - 2 beforeM0[6] - 2 beforeM0[7] + 12 Sprobx0[1]
   + 7 Sproby0[1] >= 0
 R118054: state0[4] + 2 state0[6] - beforeM0[4] - 3 beforeM0[5]
   - beforeM0[6] + 4 Sprobx0[1] + 2 Sproby0[1] >= 0
 R118055: state0[5] + beforeM0[4] - Sprobx0[1] >= 0
 R118056: 2 state0[4] + state0[5] + 2 state0[7] - beforeM0[4] - beforeM0[6]
   - beforeM0[7] + Sprobx0[1] + 2 Sproby0[1] >= 0
 R118057: state0[4] + state0[5] + state0[6] - Sprobx0[1] >= 0
 R118058: - state0[4] - state0[5] + state0[7] - beforeM0[4] - 2 beforeM0[5]
   + beforeM0[6] + beforeM0[7] + 4 Sprobx0[1] + 3 Sproby0[1] >= 0
 R118059: state0[5] - state0[6] + state0[7] + beforeM0[4] - beforeM0[5]
   - beforeM0[6] + beforeM0[7] + Sprobx0[1] + 3 Sproby0[1] >= 0
 R118060: state0[4] - state0[5] - 2 state0[6] - state0[7] + beforeM0[4]
   - 2 beforeM0[6] + 2 beforeM0[7] + 4 Sprobx0[1] + 4 Sproby0[1] >= 0
 R118061: - state0[4] + state0[5] - state0[6] + state0[7] - 4 beforeM0[4]
   - beforeM0[5] - beforeM0[7] + 7 Sprobx0[1] + 4 Sproby0[1] >= 0
 R118062: - 3 state0[4] - state0[5] - state0[6] - 2 state0[7]
   - 3 beforeM0[4] - 2 beforeM0[5] - beforeM0[6] + 2 beforeM0[7]
   + 12 Sprobx0[1] + 7 Sproby0[1] >= 0
 R118063: state0[5] + state0[6] + beforeM0[4] + beforeM0[5] - 2 Sprobx0[1]
   - Sproby0[1] >= 0
 R118064: state0[4] - 3 state0[5] - 4 state0[6] - 2 state0[7] - beforeM0[5]
   + 3 beforeM0[6] + 3 beforeM0[7] + 10 Sprobx0[1] + 2 Sproby0[1] >= 0
 R118065: 2 state0[4] + 2 state0[5] - state0[6] + 4 state0[7]
   - 5 beforeM0[4] - beforeM0[5] + beforeM0[6] + beforeM0[7] + 4 Sprobx0[1]
   + Sproby0[1] >= 0
 R118066: - state0[4] - state0[5] - 3 state0[6] + state0[7] + 2 beforeM0[5]
   + beforeM0[7] + 4 Sprobx0[1] + 2 Sproby0[1] >= 0
 R118067: - Sprobx0[2] - Sproby0[2] >= -1
 R118068: - state0[9] - state0[10] - state0[11] - beforeM0[9]
   + beforeM0[10] - beforeM0[11] + 4 Sprobx0[2] + 3 Sproby0[2] >= 0
 R118069: - 3 state0[8] - state0[10] + state0[11] - 3 beforeM0[8]
   - beforeM0[9] - 2 beforeM0[10] - 2 beforeM0[11] + 11 Sprobx0[2]
   + 7 Sproby0[2] >= 0
 R118070: - state0[9] - state0[10] - state0[11] - beforeM0[8]
   - 2 beforeM0[9] - beforeM0[10] - beforeM0[11] + 8 Sprobx0[2]
   + 4 Sproby0[2] >= 0
 R118071: - 2 state0[8] + state0[9] - 2 state0[11] - beforeM0[8]
   + 2 beforeM0[9] - beforeM0[11] + 4 Sprobx0[2] + 5 Sproby0[2] >= 0
 R118072: state0[8] - state0[9] + state0[11] - beforeM0[8] + beforeM0[9]
   + 2 beforeM0[10] - beforeM0[11] + 2 Sprobx0[2] + Sproby0[2] >= 0
 R118073: state0[8] - state0[9] - state0[11] + beforeM0[9] + beforeM0[11]
   + Sprobx0[2] + 2 Sproby0[2] >= 0
 R118074: state0[10] + beforeM0[9] - Sprobx0[2] >= 0
 R118075: - 3 state0[9] + 2 beforeM0[8] - beforeM0[9] + beforeM0[10]
   - beforeM0[11] + 4 Sprobx0[2] + 2 Sproby0[2] >= 0
 R118076: state0[9] + 2 beforeM0[8] + beforeM0[9] + beforeM0[11]
   - 2 Sprobx0[2] - Sproby0[2] >= 0
 R118077: - state0[8] - state0[9] + 2 state0[10] + beforeM0[8]
   + 2 beforeM0[10] + Sproby0[2] >= 0
 R118078: 2 state0[8] - 2 state0[9] - 2 state0[10] - 3 state0[11]
   - beforeM0[9] + beforeM0[10] - beforeM0[11] + 8 Sprobx0[2]
   + 4 Sproby0[2] >= 0
 R118079: - 3 state0[8] + state0[9] - state0[10] + state0[11]
   - 4 beforeM0[8] - beforeM0[9] - 2 beforeM0[10] - 2 beforeM0[11]
   + 12 Sprobx0[2] + 7 Sproby0[2] >= 0
 R118080: state0[8] + 2 state0[10] - beforeM0[8] - 3 beforeM0[9]
   - beforeM0[10] + 4 Sprobx0[2] + 2 Sproby0[2] >= 0
 R118081: state0[9] + beforeM0[8] - Sprobx0[2] >= 0
 R118082: 2 state0[8] + state0[9] + 2 state0[11] - beforeM0[8]
   - beforeM0[10] - beforeM0[11] + Sprobx0[2] + 2 Sproby0[2] >= 0
 R118083: state0[8] + state0[9] + state0[10] - Sprobx0[2] >= 0
 R118084: - state0[8] - state0[9] + state0[11] - beforeM0[8]
   - 2 beforeM0[9] + beforeM0[10] + beforeM0[11] + 4 Sprobx0[2]
   + 3 Sproby0[2] >= 0
 R118085: state0[9] - state0[10] + state0[11] + beforeM0[8] - beforeM0[9]
   - beforeM0[10] + beforeM0[11] + Sprobx0[2] + 3 Sproby0[2] >= 0
 R118086: state0[8] - state0[9] - 2 state0[10] - state0[11] + beforeM0[8]
   - 2 beforeM0[10] + 2 beforeM0[11] + 4 Sprobx0[2] + 4 Sproby0[2] >= 0
 R118087: - state0[8] + state0[9] - state0[10] + state0[11] - 4 beforeM0[8]
   - beforeM0[9] - beforeM0[11] + 7 Sprobx0[2] + 4 Sproby0[2] >= 0
 R118088: - 3 state0[8] - state0[9] - state0[10] - 2 state0[11]
   - 3 beforeM0[8] - 2 beforeM0[9] - beforeM0[10] + 2 beforeM0[11]
   + 12 Sprobx0[2] + 7 Sproby0[2] >= 0
 R118089: state0[9] + state0[10] + beforeM0[8] + beforeM0[9] - 2 Sprobx0[2]
   - Sproby0[2] >= 0
 R118090: state0[8] - 3 state0[9] - 4 state0[10] - 2 state0[11]
   - beforeM0[9] + 3 beforeM0[10] + 3 beforeM0[11] + 10 Sprobx0[2]
   + 2 Sproby0[2] >= 0
 R118091: 2 state0[8] + 2 state0[9] - state0[10] + 4 state0[11]
   - 5 beforeM0[8] - beforeM0[9] + beforeM0[10] + beforeM0[11]
   + 4 Sprobx0[2] + Sproby0[2] >= 0
 R118092: - state0[8] - state0[9] - 3 state0[10] + state0[11]
   + 2 beforeM0[9] + beforeM0[11] + 4 Sprobx0[2] + 2 Sproby0[2] >= 0
 R118093: - Sprobx0[3] - Sproby0[3] >= -1
 R118094: - state0[13] - state0[14] - state0[15] - beforeM0[13]
   + beforeM0[14] - beforeM0[15] + 4 Sprobx0[3] + 3 Sproby0[3] >= 0
 R118095: - 3 state0[12] - state0[14] + state0[15] - 3 beforeM0[12]
   - beforeM0[13] - 2 beforeM0[14] - 2 beforeM0[15] + 11 Sprobx0[3]
   + 7 Sproby0[3] >= 0
 R118096: - state0[13] - state0[14] - state0[15] - beforeM0[12]
   - 2 beforeM0[13] - beforeM0[14] - beforeM0[15] + 8 Sprobx0[3]
   + 4 Sproby0[3] >= 0
 R118097: - 2 state0[12] + state0[13] - 2 state0[15] - beforeM0[12]
   + 2 beforeM0[13] - beforeM0[15] + 4 Sprobx0[3] + 5 Sproby0[3] >= 0
 R118098: state0[12] - state0[13] + state0[15] - beforeM0[12]
   + beforeM0[13] + 2 beforeM0[14] - beforeM0[15] + 2 Sprobx0[3]
   + Sproby0[3] >= 0
 R118099: state0[12] - state0[13] - state0[15] + beforeM0[13]
   + beforeM0[15] + Sprobx0[3] + 2 Sproby0[3] >= 0
 R118100: state0[14] + beforeM0[13] - Sprobx0[3] >= 0
 R118101: - 3 state0[13] + 2 beforeM0[12] - beforeM0[13] + beforeM0[14]
   - beforeM0[15] + 4 Sprobx0[3] + 2 Sproby0[3] >= 0
 R118102: state0[13] + 2 beforeM0[12] + beforeM0[13] + beforeM0[15]
   - 2 Sprobx0[3] - Sproby0[3] >= 0
 R118103: - state0[12] - state0[13] + 2 state0[14] + beforeM0[12]
   + 2 beforeM0[14] + Sproby0[3] >= 0
 R118104: 2 state0[12] - 2 state0[13] - 2 state0[14] - 3 state0[15]
   - beforeM0[13] + beforeM0[14] - beforeM0[15] + 8 Sprobx0[3]
   + 4 Sproby0[3] >= 0
 R118105: - 3 state0[12] + state0[13] - state0[14] + state0[15]
   - 4 beforeM0[12] - beforeM0[13] - 2 beforeM0[14] - 2 beforeM0[15]
   + 12 Sprobx0[3] + 7 Sproby0[3] >= 0
 R118106: state0[12] + 2 state0[14] - beforeM0[12] - 3 beforeM0[13]
   - beforeM0[14] + 4 Sprobx0[3] + 2 Sproby0[3] >= 0
 R118107: state0[13] + beforeM0[12] - Sprobx0[3] >= 0
 R118108: 2 state0[12] + state0[13] + 2 state0[15] - beforeM0[12]
   - beforeM0[14] - beforeM0[15] + Sprobx0[3] + 2 Sproby0[3] >= 0
 R118109: state0[12] + state0[13] + state0[14] - Sprobx0[3] >= 0
 R118110: - state0[12] - state0[13] + state0[15] - beforeM0[12]
   - 2 beforeM0[13] + beforeM0[14] + beforeM0[15] + 4 Sprobx0[3]
   + 3 Sproby0[3] >= 0
 R118111: state0[13] - state0[14] + state0[15] + beforeM0[12]
   - beforeM0[13] - beforeM0[14] + beforeM0[15] + Sprobx0[3] + 3 Sproby0[3]
   >= 0
 R118112: state0[12] - state0[13] - 2 state0[14] - state0[15]
   + beforeM0[12] - 2 beforeM0[14] + 2 beforeM0[15] + 4 Sprobx0[3]
   + 4 Sproby0[3] >= 0
 R118113: - state0[12] + state0[13] - state0[14] + state0[15]
   - 4 beforeM0[12] - beforeM0[13] - beforeM0[15] + 7 Sprobx0[3]
   + 4 Sproby0[3] >= 0
 R118114: - 3 state0[12] - state0[13] - state0[14] - 2 state0[15]
   - 3 beforeM0[12] - 2 beforeM0[13] - beforeM0[14] + 2 beforeM0[15]
   + 12 Sprobx0[3] + 7 Sproby0[3] >= 0
 R118115: state0[13] + state0[14] + beforeM0[12] + beforeM0[13]
   - 2 Sprobx0[3] - Sproby0[3] >= 0
 R118116: state0[12] - 3 state0[13] - 4 state0[14] - 2 state0[15]
   - beforeM0[13] + 3 beforeM0[14] + 3 beforeM0[15] + 10 Sprobx0[3]
   + 2 Sproby0[3] >= 0
 R118117: 2 state0[12] + 2 state0[13] - state0[14] + 4 state0[15]
   - 5 beforeM0[12] - beforeM0[13] + beforeM0[14] + beforeM0[15]
   + 4 Sprobx0[3] + Sproby0[3] >= 0
 R118118: - state0[12] - state0[13] - 3 state0[14] + state0[15]
   + 2 beforeM0[13] + beforeM0[15] + 4 Sprobx0[3] + 2 Sproby0[3] >= 0
 R118119: - Sprobx0[4] - Sproby0[4] >= -1
 R118120: - state0[33] - state0[34] - state0[35] - beforeM0[17]
   + beforeM0[18] - beforeM0[19] + 4 Sprobx0[4] + 3 Sproby0[4] >= 0
 R118121: - 3 state0[32] - state0[34] + state0[35] - 3 beforeM0[16]
   - beforeM0[17] - 2 beforeM0[18] - 2 beforeM0[19] + 11 Sprobx0[4]
   + 7 Sproby0[4] >= 0
 R118122: - state0[33] - state0[34] - state0[35] - beforeM0[16]
   - 2 beforeM0[17] - beforeM0[18] - beforeM0[19] + 8 Sprobx0[4]
   + 4 Sproby0[4] >= 0
 R118123: - 2 state0[32] + state0[33] - 2 state0[35] - beforeM0[16]
   + 2 beforeM0[17] - beforeM0[19] + 4 Sprobx0[4] + 5 Sproby0[4] >= 0
 R118124: state0[32] - state0[33] + state0[35] - beforeM0[16]
   + beforeM0[17] + 2 beforeM0[18] - beforeM0[19] + 2 Sprobx0[4]
   + Sproby0[4] >= 0
 R118125: state0[32] - state0[33] - state0[35] + beforeM0[17]
   + beforeM0[19] + Sprobx0[4] + 2 Sproby0[4] >= 0
 R118126: state0[34] + beforeM0[17] - Sprobx0[4] >= 0
 R118127: - 3 state0[33] + 2 beforeM0[16] - beforeM0[17] + beforeM0[18]
   - beforeM0[19] + 4 Sprobx0[4] + 2 Sproby0[4] >= 0
 R118128: state0[33] + 2 beforeM0[16] + beforeM0[17] + beforeM0[19]
   - 2 Sprobx0[4] - Sproby0[4] >= 0
 R118129: - state0[32] - state0[33] + 2 state0[34] + beforeM0[16]
   + 2 beforeM0[18] + Sproby0[4] >= 0
 R118130: 2 state0[32] - 2 state0[33] - 2 state0[34] - 3 state0[35]
   - beforeM0[17] + beforeM0[18] - beforeM0[19] + 8 Sprobx0[4]
   + 4 Sproby0[4] >= 0
 R118131: - 3 state0[32] + state0[33] - state0[34] + state0[35]
   - 4 beforeM0[16] - beforeM0[17] - 2 beforeM0[18] - 2 beforeM0[19]
   + 12 Sprobx0[4] + 7 Sproby0[4] >= 0
 R118132: state0[32] + 2 state0[34] - beforeM0[16] - 3 beforeM0[17]
   - beforeM0[18] + 4 Sprobx0[4] + 2 Sproby0[4] >= 0
 R118133: state0[33] + beforeM0[16] - Sprobx0[4] >= 0
 R118134: 2 state0[32] + state0[33] + 2 state0[35] - beforeM0[16]
   - beforeM0[18] - beforeM0[19] + Sprobx0[4] + 2 Sproby0[4] >= 0
 R118135: state0[32] + state0[33] + state0[34] - Sprobx0[4] >= 0
 R118136: - state0[32] - state0[33] + state0[35] - beforeM0[16]
   - 2 beforeM0[17] + beforeM0[18] + beforeM0[19] + 4 Sprobx0[4]
   + 3 Sproby0[4] >= 0
 R118137: state0[33] - state0[34] + state0[35] + beforeM0[16]
   - beforeM0[17] - beforeM0[18] + beforeM0[19] + Sprobx0[4] + 3 Sproby0[4]
   >= 0
 R118138: state0[32] - state0[33] - 2 state0[34] - state0[35]
   + beforeM0[16] - 2 beforeM0[18] + 2 beforeM0[19] + 4 Sprobx0[4]
   + 4 Sproby0[4] >= 0
 R118139: - state0[32] + state0[33] - state0[34] + state0[35]
   - 4 beforeM0[16] - beforeM0[17] - beforeM0[19] + 7 Sprobx0[4]
   + 4 Sproby0[4] >= 0
 R118140: - 3 state0[32] - state0[33] - state0[34] - 2 state0[35]
   - 3 beforeM0[16] - 2 beforeM0[17] - beforeM0[18] + 2 beforeM0[19]
   + 12 Sprobx0[4] + 7 Sproby0[4] >= 0
 R118141: state0[33] + state0[34] + beforeM0[16] + beforeM0[17]
   - 2 Sprobx0[4] - Sproby0[4] >= 0
 R118142: state0[32] - 3 state0[33] - 4 state0[34] - 2 state0[35]
   - beforeM0[17] + 3 beforeM0[18] + 3 beforeM0[19] + 10 Sprobx0[4]
   + 2 Sproby0[4] >= 0
 R118143: 2 state0[32] + 2 state0[33] - state0[34] + 4 state0[35]
   - 5 beforeM0[16] - beforeM0[17] + beforeM0[18] + beforeM0[19]
   + 4 Sprobx0[4] + Sproby0[4] >= 0
 R118144: - state0[32] - state0[33] - 3 state0[34] + state0[35]
   + 2 beforeM0[17] + beforeM0[19] + 4 Sprobx0[4] + 2 Sproby0[4] >= 0
 R118145: - Sprobx0[5] - Sproby0[5] >= -1
 R118146: - state0[37] - state0[38] - state0[39] - beforeM0[21]
   + beforeM0[22] - beforeM0[23] + 4 Sprobx0[5] + 3 Sproby0[5] >= 0
 R118147: - 3 state0[36] - state0[38] + state0[39] - 3 beforeM0[20]
   - beforeM0[21] - 2 beforeM0[22] - 2 beforeM0[23] + 11 Sprobx0[5]
   + 7 Sproby0[5] >= 0
 R118148: - state0[37] - state0[38] - state0[39] - beforeM0[20]
   - 2 beforeM0[21] - beforeM0[22] - beforeM0[23] + 8 Sprobx0[5]
   + 4 Sproby0[5] >= 0
 R118149: - 2 state0[36] + state0[37] - 2 state0[39] - beforeM0[20]
   + 2 beforeM0[21] - beforeM0[23] + 4 Sprobx0[5] + 5 Sproby0[5] >= 0
 R118150: state0[36] - state0[37] + state0[39] - beforeM0[20]
   + beforeM0[21] + 2 beforeM0[22] - beforeM0[23] + 2 Sprobx0[5]
   + Sproby0[5] >= 0
 R118151: state0[36] - state0[37] - state0[39] + beforeM0[21]
   + beforeM0[23] + Sprobx0[5] + 2 Sproby0[5] >= 0
 R118152: state0[38] + beforeM0[21] - Sprobx0[5] >= 0
 R118153: - 3 state0[37] + 2 beforeM0[20] - beforeM0[21] + beforeM0[22]
   - beforeM0[23] + 4 Sprobx0[5] + 2 Sproby0[5] >= 0
 R118154: state0[37] + 2 beforeM0[20] + beforeM0[21] + beforeM0[23]
   - 2 Sprobx0[5] - Sproby0[5] >= 0
 R118155: - state0[36] - state0[37] + 2 state0[38] + beforeM0[20]
   + 2 beforeM0[22] + Sproby0[5] >= 0
 R118156: 2 state0[36] - 2 state0[37] - 2 state0[38] - 3 state0[39]
   - beforeM0[21] + beforeM0[22] - beforeM0[23] + 8 Sprobx0[5]
   + 4 Sproby0[5] >= 0
 R118157: - 3 state0[36] + state0[37] - state0[38] + state0[39]
   - 4 beforeM0[20] - beforeM0[21] - 2 beforeM0[22] - 2 beforeM0[23]
   + 12 Sprobx0[5] + 7 Sproby0[5] >= 0
 R118158: state0[36] + 2 state0[38] - beforeM0[20] - 3 beforeM0[21]
   - beforeM0[22] + 4 Sprobx0[5] + 2 Sproby0[5] >= 0
 R118159: state0[37] + beforeM0[20] - Sprobx0[5] >= 0
 R118160: 2 state0[36] + state0[37] + 2 state0[39] - beforeM0[20]
   - beforeM0[22] - beforeM0[23] + Sprobx0[5] + 2 Sproby0[5] >= 0
 R118161: state0[36] + state0[37] + state0[38] - Sprobx0[5] >= 0
 R118162: - state0[36] - state0[37] + state0[39] - beforeM0[20]
   - 2 beforeM0[21] + beforeM0[22] + beforeM0[23] + 4 Sprobx0[5]
   + 3 Sproby0[5] >= 0
 R118163: state0[37] - state0[38] + state0[39] + beforeM0[20]
   - beforeM0[21] - beforeM0[22] + beforeM0[23] + Sprobx0[5] + 3 Sproby0[5]
   >= 0
 R118164: state0[36] - state0[37] - 2 state0[38] - state0[39]
   + beforeM0[20] - 2 beforeM0[22] + 2 beforeM0[23] + 4 Sprobx0[5]
   + 4 Sproby0[5] >= 0
 R118165: - state0[36] + state0[37] - state0[38] + state0[39]
   - 4 beforeM0[20] - beforeM0[21] - beforeM0[23] + 7 Sprobx0[5]
   + 4 Sproby0[5] >= 0
 R118166: - 3 state0[36] - state0[37] - state0[38] - 2 state0[39]
   - 3 beforeM0[20] - 2 beforeM0[21] - beforeM0[22] + 2 beforeM0[23]
   + 12 Sprobx0[5] + 7 Sproby0[5] >= 0
 R118167: state0[37] + state0[38] + beforeM0[20] + beforeM0[21]
   - 2 Sprobx0[5] - Sproby0[5] >= 0
 R118168: state0[36] - 3 state0[37] - 4 state0[38] - 2 state0[39]
   - beforeM0[21] + 3 beforeM0[22] + 3 beforeM0[23] + 10 Sprobx0[5]
   + 2 Sproby0[5] >= 0
 R118169: 2 state0[36] + 2 state0[37] - state0[38] + 4 state0[39]
   - 5 beforeM0[20] - beforeM0[21] + beforeM0[22] + beforeM0[23]
   + 4 Sprobx0[5] + Sproby0[5] >= 0
 R118170: - state0[36] - state0[37] - 3 state0[38] + state0[39]
   + 2 beforeM0[21] + beforeM0[23] + 4 Sprobx0[5] + 2 Sproby0[5] >= 0
 R118171: - Sprobx0[6] - Sproby0[6] >= -1
 R118172: - state0[41] - state0[42] - state0[43] - beforeM0[25]
   + beforeM0[26] - beforeM0[27] + 4 Sprobx0[6] + 3 Sproby0[6] >= 0
 R118173: - 3 state0[40] - state0[42] + state0[43] - 3 beforeM0[24]
   - beforeM0[25] - 2 beforeM0[26] - 2 beforeM0[27] + 11 Sprobx0[6]
   + 7 Sproby0[6] >= 0
 R118174: - state0[41] - state0[42] - state0[43] - beforeM0[24]
   - 2 beforeM0[25] - beforeM0[26] - beforeM0[27] + 8 Sprobx0[6]
   + 4 Sproby0[6] >= 0
 R118175: - 2 state0[40] + state0[41] - 2 state0[43] - beforeM0[24]
   + 2 beforeM0[25] - beforeM0[27] + 4 Sprobx0[6] + 5 Sproby0[6] >= 0
 R118176: state0[40] - state0[41] + state0[43] - beforeM0[24]
   + beforeM0[25] + 2 beforeM0[26] - beforeM0[27] + 2 Sprobx0[6]
   + Sproby0[6] >= 0
 R118177: state0[40] - state0[41] - state0[43] + beforeM0[25]
   + beforeM0[27] + Sprobx0[6] + 2 Sproby0[6] >= 0
 R118178: state0[42] + beforeM0[25] - Sprobx0[6] >= 0
 R118179: - 3 state0[41] + 2 beforeM0[24] - beforeM0[25] + beforeM0[26]
   - beforeM0[27] + 4 Sprobx0[6] + 2 Sproby0[6] >= 0
 R118180: state0[41] + 2 beforeM0[24] + beforeM0[25] + beforeM0[27]
   - 2 Sprobx0[6] - Sproby0[6] >= 0
 R118181: - state0[40] - state0[41] + 2 state0[42] + beforeM0[24]
   + 2 beforeM0[26] + Sproby0[6] >= 0
 R118182: 2 state0[40] - 2 state0[41] - 2 state0[42] - 3 state0[43]
   - beforeM0[25] + beforeM0[26] - beforeM0[27] + 8 Sprobx0[6]
   + 4 Sproby0[6] >= 0
 R118183: - 3 state0[40] + state0[41] - state0[42] + state0[43]
   - 4 beforeM0[24] - beforeM0[25] - 2 beforeM0[26] - 2 beforeM0[27]
   + 12 Sprobx0[6] + 7 Sproby0[6] >= 0
 R118184: state0[40] + 2 state0[42] - beforeM0[24] - 3 beforeM0[25]
   - beforeM0[26] + 4 Sprobx0[6] + 2 Sproby0[6] >= 0
 R118185: state0[41] + beforeM0[24] - Sprobx0[6] >= 0
 R118186: 2 state0[40] + state0[41] + 2 state0[43] - beforeM0[24]
   - beforeM0[26] - beforeM0[27] + Sprobx0[6] + 2 Sproby0[6] >= 0
 R118187: state0[40] + state0[41] + state0[42] - Sprobx0[6] >= 0
 R118188: - state0[40] - state0[41] + state0[43] - beforeM0[24]
   - 2 beforeM0[25] + beforeM0[26] + beforeM0[27] + 4 Sprobx0[6]
   + 3 Sproby0[6] >= 0
 R118189: state0[41] - state0[42] + state0[43] + beforeM0[24]
   - beforeM0[25] - beforeM0[26] + beforeM0[27] + Sprobx0[6] + 3 Sproby0[6]
   >= 0
 R118190: state0[40] - state0[41] - 2 state0[42] - state0[43]
   + beforeM0[24] - 2 beforeM0[26] + 2 beforeM0[27] + 4 Sprobx0[6]
   + 4 Sproby0[6] >= 0
 R118191: - state0[40] + state0[41] - state0[42] + state0[43]
   - 4 beforeM0[24] - beforeM0[25] - beforeM0[27] + 7 Sprobx0[6]
   + 4 Sproby0[6] >= 0
 R118192: - 3 state0[40] - state0[41] - state0[42] - 2 state0[43]
   - 3 beforeM0[24] - 2 beforeM0[25] - beforeM0[26] + 2 beforeM0[27]
   + 12 Sprobx0[6] + 7 Sproby0[6] >= 0
 R118193: state0[41] + state0[42] + beforeM0[24] + beforeM0[25]
   - 2 Sprobx0[6] - Sproby0[6] >= 0
 R118194: state0[40] - 3 state0[41] - 4 state0[42] - 2 state0[43]
   - beforeM0[25] + 3 beforeM0[26] + 3 beforeM0[27] + 10 Sprobx0[6]
   + 2 Sproby0[6] >= 0
 R118195: 2 state0[40] + 2 state0[41] - state0[42] + 4 state0[43]
   - 5 beforeM0[24] - beforeM0[25] + beforeM0[26] + beforeM0[27]
   + 4 Sprobx0[6] + Sproby0[6] >= 0
 R118196: - state0[40] - state0[41] - 3 state0[42] + state0[43]
   + 2 beforeM0[25] + beforeM0[27] + 4 Sprobx0[6] + 2 Sproby0[6] >= 0
 R118197: - Sprobx0[7] - Sproby0[7] >= -1
 R118198: - state0[45] - state0[46] - state0[47] - beforeM0[29]
   + beforeM0[30] - beforeM0[31] + 4 Sprobx0[7] + 3 Sproby0[7] >= 0
 R118199: - 3 state0[44] - state0[46] + state0[47] - 3 beforeM0[28]
   - beforeM0[29] - 2 beforeM0[30] - 2 beforeM0[31] + 11 Sprobx0[7]
   + 7 Sproby0[7] >= 0
 R118200: - state0[45] - state0[46] - state0[47] - beforeM0[28]
   - 2 beforeM0[29] - beforeM0[30] - beforeM0[31] + 8 Sprobx0[7]
   + 4 Sproby0[7] >= 0
 R118201: - 2 state0[44] + state0[45] - 2 state0[47] - beforeM0[28]
   + 2 beforeM0[29] - beforeM0[31] + 4 Sprobx0[7] + 5 Sproby0[7] >= 0
 R118202: state0[44] - state0[45] + state0[47] - beforeM0[28]
   + beforeM0[29] + 2 beforeM0[30] - beforeM0[31] + 2 Sprobx0[7]
   + Sproby0[7] >= 0
 R118203: state0[44] - state0[45] - state0[47] + beforeM0[29]
   + beforeM0[31] + Sprobx0[7] + 2 Sproby0[7] >= 0
 R118204: state0[46] + beforeM0[29] - Sprobx0[7] >= 0
 R118205: - 3 state0[45] + 2 beforeM0[28] - beforeM0[29] + beforeM0[30]
   - beforeM0[31] + 4 Sprobx0[7] + 2 Sproby0[7] >= 0
 R118206: state0[45] + 2 beforeM0[28] + beforeM0[29] + beforeM0[31]
   - 2 Sprobx0[7] - Sproby0[7] >= 0
 R118207: - state0[44] - state0[45] + 2 state0[46] + beforeM0[28]
   + 2 beforeM0[30] + Sproby0[7] >= 0
 R118208: 2 state0[44] - 2 state0[45] - 2 state0[46] - 3 state0[47]
   - beforeM0[29] + beforeM0[30] - beforeM0[31] + 8 Sprobx0[7]
   + 4 Sproby0[7] >= 0
 R118209: - 3 state0[44] + state0[45] - state0[46] + state0[47]
   - 4 beforeM0[28] - beforeM0[29] - 2 beforeM0[30] - 2 beforeM0[31]
   + 12 Sprobx0[7] + 7 Sproby0[7] >= 0
 R118210: state0[44] + 2 state0[46] - beforeM0[28] - 3 beforeM0[29]
   - beforeM0[30] + 4 Sprobx0[7] + 2 Sproby0[7] >= 0
 R118211: state0[45] + beforeM0[28] - Sprobx0[7] >= 0
 R118212: 2 state0[44] + state0[45] + 2 state0[47] - beforeM0[28]
   - beforeM0[30] - beforeM0[31] + Sprobx0[7] + 2 Sproby0[7] >= 0
 R118213: state0[44] + state0[45] + state0[46] - Sprobx0[7] >= 0
 R118214: - state0[44] - state0[45] + state0[47] - beforeM0[28]
   - 2 beforeM0[29] + beforeM0[30] + beforeM0[31] + 4 Sprobx0[7]
   + 3 Sproby0[7] >= 0
 R118215: state0[45] - state0[46] + state0[47] + beforeM0[28]
   - beforeM0[29] - beforeM0[30] + beforeM0[31] + Sprobx0[7] + 3 Sproby0[7]
   >= 0
 R118216: state0[44] - state0[45] - 2 state0[46] - state0[47]
   + beforeM0[28] - 2 beforeM0[30] + 2 beforeM0[31] + 4 Sprobx0[7]
   + 4 Sproby0[7] >= 0
 R118217: - state0[44] + state0[45] - state0[46] + state0[47]
   - 4 beforeM0[28] - beforeM0[29] - beforeM0[31] + 7 Sprobx0[7]
   + 4 Sproby0[7] >= 0
 R118218: - 3 state0[44] - state0[45] - state0[46] - 2 state0[47]
   - 3 beforeM0[28] - 2 beforeM0[29] - beforeM0[30] + 2 beforeM0[31]
   + 12 Sprobx0[7] + 7 Sproby0[7] >= 0
 R118219: state0[45] + state0[46] + beforeM0[28] + beforeM0[29]
   - 2 Sprobx0[7] - Sproby0[7] >= 0
 R118220: state0[44] - 3 state0[45] - 4 state0[46] - 2 state0[47]
   - beforeM0[29] + 3 beforeM0[30] + 3 beforeM0[31] + 10 Sprobx0[7]
   + 2 Sproby0[7] >= 0
 R118221: 2 state0[44] + 2 state0[45] - state0[46] + 4 state0[47]
   - 5 beforeM0[28] - beforeM0[29] + beforeM0[30] + beforeM0[31]
   + 4 Sprobx0[7] + Sproby0[7] >= 0
 R118222: - state0[44] - state0[45] - 3 state0[46] + state0[47]
   + 2 beforeM0[29] + beforeM0[31] + 4 Sprobx0[7] + 2 Sproby0[7] >= 0
 R118223: beforeM0[1] + beforeM0[4] + beforeM0[5] + beforeM0[8]
   + beforeM0[12] - afterM0[0] - 2 dummy0[0] = 0
 R118224: beforeM0[2] + beforeM0[5] + beforeM0[6] + beforeM0[9]
   + beforeM0[13] - afterM0[1] - 2 dummy0[1] = 0
 R118225: beforeM0[0] + beforeM0[3] + beforeM0[4] + beforeM0[6]
   + beforeM0[7] + beforeM0[10] + beforeM0[14] - afterM0[2] - 2 dummy0[2]
   = 0
 R118226: beforeM0[0] + beforeM0[4] + beforeM0[7] + beforeM0[11]
   + beforeM0[15] - afterM0[3] - 2 dummy0[3] = 0
 R118227: beforeM0[0] + beforeM0[5] + beforeM0[8] + beforeM0[9]
   + beforeM0[12] - afterM0[4] - 2 dummy0[4] = 0
 R118228: beforeM0[1] + beforeM0[6] + beforeM0[9] + beforeM0[10]
   + beforeM0[13] - afterM0[5] - 2 dummy0[5] = 0
 R118229: beforeM0[2] + beforeM0[4] + beforeM0[7] + beforeM0[8]
   + beforeM0[10] + beforeM0[11] + beforeM0[14] - afterM0[6] - 2 dummy0[6]
   = 0
 R118230: beforeM0[3] + beforeM0[4] + beforeM0[8] + beforeM0[11]
   + beforeM0[15] - afterM0[7] - 2 dummy0[7] = 0
 R118231: beforeM0[0] + beforeM0[4] + beforeM0[9] + beforeM0[12]
   + beforeM0[13] - afterM0[8] - 2 dummy0[8] = 0
 R118232: beforeM0[1] + beforeM0[5] + beforeM0[10] + beforeM0[13]
   + beforeM0[14] - afterM0[9] - 2 dummy0[9] = 0
 R118233: beforeM0[2] + beforeM0[6] + beforeM0[8] + beforeM0[11]
   + beforeM0[12] + beforeM0[14] + beforeM0[15] - afterM0[10]
   - 2 dummy0[10] = 0
 R118234: beforeM0[3] + beforeM0[7] + beforeM0[8] + beforeM0[12]
   + beforeM0[15] - afterM0[11] - 2 dummy0[11] = 0
 R118235: beforeM0[0] + beforeM0[1] + beforeM0[4] + beforeM0[8]
   + beforeM0[13] - afterM0[12] - 2 dummy0[12] = 0
 R118236: beforeM0[1] + beforeM0[2] + beforeM0[5] + beforeM0[9]
   + beforeM0[14] - afterM0[13] - 2 dummy0[13] = 0
 R118237: beforeM0[0] + beforeM0[2] + beforeM0[3] + beforeM0[6]
   + beforeM0[10] + beforeM0[12] + beforeM0[15] - afterM0[14]
   - 2 dummy0[14] = 0
 R118238: beforeM0[0] + beforeM0[3] + beforeM0[7] + beforeM0[11]
   + beforeM0[12] - afterM0[15] - 2 dummy0[15] = 0
 R118239: beforeM0[17] + beforeM0[20] + beforeM0[21] + beforeM0[24]
   + beforeM0[28] - afterM0[16] - 2 dummy0[16] = 0
 R118240: beforeM0[18] + beforeM0[21] + beforeM0[22] + beforeM0[25]
   + beforeM0[29] - afterM0[17] - 2 dummy0[17] = 0
 R118241: beforeM0[16] + beforeM0[19] + beforeM0[20] + beforeM0[22]
   + beforeM0[23] + beforeM0[26] + beforeM0[30] - afterM0[18]
   - 2 dummy0[18] = 0
 R118242: beforeM0[16] + beforeM0[20] + beforeM0[23] + beforeM0[27]
   + beforeM0[31] - afterM0[19] - 2 dummy0[19] = 0
 R118243: beforeM0[16] + beforeM0[21] + beforeM0[24] + beforeM0[25]
   + beforeM0[28] - afterM0[20] - 2 dummy0[20] = 0
 R118244: beforeM0[17] + beforeM0[22] + beforeM0[25] + beforeM0[26]
   + beforeM0[29] - afterM0[21] - 2 dummy0[21] = 0
 R118245: beforeM0[18] + beforeM0[20] + beforeM0[23] + beforeM0[24]
   + beforeM0[26] + beforeM0[27] + beforeM0[30] - afterM0[22]
   - 2 dummy0[22] = 0
 R118246: beforeM0[19] + beforeM0[20] + beforeM0[24] + beforeM0[27]
   + beforeM0[31] - afterM0[23] - 2 dummy0[23] = 0
 R118247: beforeM0[16] + beforeM0[20] + beforeM0[25] + beforeM0[28]
   + beforeM0[29] - afterM0[24] - 2 dummy0[24] = 0
 R118248: beforeM0[17] + beforeM0[21] + beforeM0[26] + beforeM0[29]
   + beforeM0[30] - afterM0[25] - 2 dummy0[25] = 0
 R118249: beforeM0[18] + beforeM0[22] + beforeM0[24] + beforeM0[27]
   + beforeM0[28] + beforeM0[30] + beforeM0[31] - afterM0[26]
   - 2 dummy0[26] = 0
 R118250: beforeM0[19] + beforeM0[23] + beforeM0[24] + beforeM0[28]
   + beforeM0[31] - afterM0[27] - 2 dummy0[27] = 0
 R118251: beforeM0[16] + beforeM0[17] + beforeM0[20] + beforeM0[24]
   + beforeM0[29] - afterM0[28] - 2 dummy0[28] = 0
 R118252: beforeM0[17] + beforeM0[18] + beforeM0[21] + beforeM0[25]
   + beforeM0[30] - afterM0[29] - 2 dummy0[29] = 0
 R118253: beforeM0[16] + beforeM0[18] + beforeM0[19] + beforeM0[22]
   + beforeM0[26] + beforeM0[28] + beforeM0[31] - afterM0[30]
   - 2 dummy0[30] = 0
 R118254: beforeM0[16] + beforeM0[19] + beforeM0[23] + beforeM0[27]
   + beforeM0[28] - afterM0[31] - 2 dummy0[31] = 0
 R118255: - Sprobx0[8] - Sproby0[8] >= -1
 R118256: 4 Sprobx0[8] + 3 Sproby0[8] - afterM0[1] - afterM0[2]
   - afterM0[3] - Fout0[1] + Fout0[2] - Fout0[3] >= 0
 R118257: 11 Sprobx0[8] + 7 Sproby0[8] - 3 afterM0[0] - afterM0[2]
   + afterM0[3] - 3 Fout0[0] - Fout0[1] - 2 Fout0[2] - 2 Fout0[3] >= 0
 R118258: 8 Sprobx0[8] + 4 Sproby0[8] - afterM0[1] - afterM0[2]
   - afterM0[3] - Fout0[0] - 2 Fout0[1] - Fout0[2] - Fout0[3] >= 0
 R118259: 4 Sprobx0[8] + 5 Sproby0[8] - 2 afterM0[0] + afterM0[1]
   - 2 afterM0[3] - Fout0[0] + 2 Fout0[1] - Fout0[3] >= 0
 R118260: 2 Sprobx0[8] + Sproby0[8] + afterM0[0] - afterM0[1] + afterM0[3]
   - Fout0[0] + Fout0[1] + 2 Fout0[2] - Fout0[3] >= 0
 R118261: Sprobx0[8] + 2 Sproby0[8] + afterM0[0] - afterM0[1] - afterM0[3]
   + Fout0[1] + Fout0[3] >= 0
 R118262: - Sprobx0[8] + afterM0[2] + Fout0[1] >= 0
 R118263: 4 Sprobx0[8] + 2 Sproby0[8] - 3 afterM0[1] + 2 Fout0[0]
   - Fout0[1] + Fout0[2] - Fout0[3] >= 0
 R118264: - 2 Sprobx0[8] - Sproby0[8] + afterM0[1] + 2 Fout0[0] + Fout0[1]
   + Fout0[3] >= 0
 R118265: Sproby0[8] - afterM0[0] - afterM0[1] + 2 afterM0[2] + Fout0[0]
   + 2 Fout0[2] >= 0
 R118266: 8 Sprobx0[8] + 4 Sproby0[8] + 2 afterM0[0] - 2 afterM0[1]
   - 2 afterM0[2] - 3 afterM0[3] - Fout0[1] + Fout0[2] - Fout0[3] >= 0
 R118267: 12 Sprobx0[8] + 7 Sproby0[8] - 3 afterM0[0] + afterM0[1]
   - afterM0[2] + afterM0[3] - 4 Fout0[0] - Fout0[1] - 2 Fout0[2]
   - 2 Fout0[3] >= 0
 R118268: 4 Sprobx0[8] + 2 Sproby0[8] + afterM0[0] + 2 afterM0[2]
   - Fout0[0] - 3 Fout0[1] - Fout0[2] >= 0
 R118269: - Sprobx0[8] + afterM0[1] + Fout0[0] >= 0
 R118270: Sprobx0[8] + 2 Sproby0[8] + 2 afterM0[0] + afterM0[1]
   + 2 afterM0[3] - Fout0[0] - Fout0[2] - Fout0[3] >= 0
 R118271: - Sprobx0[8] + afterM0[0] + afterM0[1] + afterM0[2] >= 0
 R118272: 4 Sprobx0[8] + 3 Sproby0[8] - afterM0[0] - afterM0[1]
   + afterM0[3] - Fout0[0] - 2 Fout0[1] + Fout0[2] + Fout0[3] >= 0
 R118273: Sprobx0[8] + 3 Sproby0[8] + afterM0[1] - afterM0[2] + afterM0[3]
   + Fout0[0] - Fout0[1] - Fout0[2] + Fout0[3] >= 0
 R118274: 4 Sprobx0[8] + 4 Sproby0[8] + afterM0[0] - afterM0[1]
   - 2 afterM0[2] - afterM0[3] + Fout0[0] - 2 Fout0[2] + 2 Fout0[3] >= 0
 R118275: 7 Sprobx0[8] + 4 Sproby0[8] - afterM0[0] + afterM0[1]
   - afterM0[2] + afterM0[3] - 4 Fout0[0] - Fout0[1] - Fout0[3] >= 0
 R118276: 12 Sprobx0[8] + 7 Sproby0[8] - 3 afterM0[0] - afterM0[1]
   - afterM0[2] - 2 afterM0[3] - 3 Fout0[0] - 2 Fout0[1] - Fout0[2]
   + 2 Fout0[3] >= 0
 R118277: - 2 Sprobx0[8] - Sproby0[8] + afterM0[1] + afterM0[2] + Fout0[0]
   + Fout0[1] >= 0
 R118278: 10 Sprobx0[8] + 2 Sproby0[8] + afterM0[0] - 3 afterM0[1]
   - 4 afterM0[2] - 2 afterM0[3] - Fout0[1] + 3 Fout0[2] + 3 Fout0[3] >= 0
 R118279: 4 Sprobx0[8] + Sproby0[8] + 2 afterM0[0] + 2 afterM0[1]
   - afterM0[2] + 4 afterM0[3] - 5 Fout0[0] - Fout0[1] + Fout0[2]
   + Fout0[3] >= 0
 R118280: 4 Sprobx0[8] + 2 Sproby0[8] - afterM0[0] - afterM0[1]
   - 3 afterM0[2] + afterM0[3] + 2 Fout0[1] + Fout0[3] >= 0
 R118281: - Sprobx0[9] - Sproby0[9] >= -1
 R118282: 4 Sprobx0[9] + 3 Sproby0[9] - afterM0[5] - afterM0[6]
   - afterM0[7] - Fout0[5] + Fout0[6] - Fout0[7] >= 0
 R118283: 11 Sprobx0[9] + 7 Sproby0[9] - 3 afterM0[4] - afterM0[6]
   + afterM0[7] - 3 Fout0[4] - Fout0[5] - 2 Fout0[6] - 2 Fout0[7] >= 0
 R118284: 8 Sprobx0[9] + 4 Sproby0[9] - afterM0[5] - afterM0[6]
   - afterM0[7] - Fout0[4] - 2 Fout0[5] - Fout0[6] - Fout0[7] >= 0
 R118285: 4 Sprobx0[9] + 5 Sproby0[9] - 2 afterM0[4] + afterM0[5]
   - 2 afterM0[7] - Fout0[4] + 2 Fout0[5] - Fout0[7] >= 0
 R118286: 2 Sprobx0[9] + Sproby0[9] + afterM0[4] - afterM0[5] + afterM0[7]
   - Fout0[4] + Fout0[5] + 2 Fout0[6] - Fout0[7] >= 0
 R118287: Sprobx0[9] + 2 Sproby0[9] + afterM0[4] - afterM0[5] - afterM0[7]
   + Fout0[5] + Fout0[7] >= 0
 R118288: - Sprobx0[9] + afterM0[6] + Fout0[5] >= 0
 R118289: 4 Sprobx0[9] + 2 Sproby0[9] - 3 afterM0[5] + 2 Fout0[4]
   - Fout0[5] + Fout0[6] - Fout0[7] >= 0
 R118290: - 2 Sprobx0[9] - Sproby0[9] + afterM0[5] + 2 Fout0[4] + Fout0[5]
   + Fout0[7] >= 0
 R118291: Sproby0[9] - afterM0[4] - afterM0[5] + 2 afterM0[6] + Fout0[4]
   + 2 Fout0[6] >= 0
 R118292: 8 Sprobx0[9] + 4 Sproby0[9] + 2 afterM0[4] - 2 afterM0[5]
   - 2 afterM0[6] - 3 afterM0[7] - Fout0[5] + Fout0[6] - Fout0[7] >= 0
 R118293: 12 Sprobx0[9] + 7 Sproby0[9] - 3 afterM0[4] + afterM0[5]
   - afterM0[6] + afterM0[7] - 4 Fout0[4] - Fout0[5] - 2 Fout0[6]
   - 2 Fout0[7] >= 0
 R118294: 4 Sprobx0[9] + 2 Sproby0[9] + afterM0[4] + 2 afterM0[6]
   - Fout0[4] - 3 Fout0[5] - Fout0[6] >= 0
 R118295: - Sprobx0[9] + afterM0[5] + Fout0[4] >= 0
 R118296: Sprobx0[9] + 2 Sproby0[9] + 2 afterM0[4] + afterM0[5]
   + 2 afterM0[7] - Fout0[4] - Fout0[6] - Fout0[7] >= 0
 R118297: - Sprobx0[9] + afterM0[4] + afterM0[5] + afterM0[6] >= 0
 R118298: 4 Sprobx0[9] + 3 Sproby0[9] - afterM0[4] - afterM0[5]
   + afterM0[7] - Fout0[4] - 2 Fout0[5] + Fout0[6] + Fout0[7] >= 0
 R118299: Sprobx0[9] + 3 Sproby0[9] + afterM0[5] - afterM0[6] + afterM0[7]
   + Fout0[4] - Fout0[5] - Fout0[6] + Fout0[7] >= 0
 R118300: 4 Sprobx0[9] + 4 Sproby0[9] + afterM0[4] - afterM0[5]
   - 2 afterM0[6] - afterM0[7] + Fout0[4] - 2 Fout0[6] + 2 Fout0[7] >= 0
 R118301: 7 Sprobx0[9] + 4 Sproby0[9] - afterM0[4] + afterM0[5]
   - afterM0[6] + afterM0[7] - 4 Fout0[4] - Fout0[5] - Fout0[7] >= 0
 R118302: 12 Sprobx0[9] + 7 Sproby0[9] - 3 afterM0[4] - afterM0[5]
   - afterM0[6] - 2 afterM0[7] - 3 Fout0[4] - 2 Fout0[5] - Fout0[6]
   + 2 Fout0[7] >= 0
 R118303: - 2 Sprobx0[9] - Sproby0[9] + afterM0[5] + afterM0[6] + Fout0[4]
   + Fout0[5] >= 0
 R118304: 10 Sprobx0[9] + 2 Sproby0[9] + afterM0[4] - 3 afterM0[5]
   - 4 afterM0[6] - 2 afterM0[7] - Fout0[5] + 3 Fout0[6] + 3 Fout0[7] >= 0
 R118305: 4 Sprobx0[9] + Sproby0[9] + 2 afterM0[4] + 2 afterM0[5]
   - afterM0[6] + 4 afterM0[7] - 5 Fout0[4] - Fout0[5] + Fout0[6]
   + Fout0[7] >= 0
 R118306: 4 Sprobx0[9] + 2 Sproby0[9] - afterM0[4] - afterM0[5]
   - 3 afterM0[6] + afterM0[7] + 2 Fout0[5] + Fout0[7] >= 0
 R118307: - Sprobx0[10] - Sproby0[10] >= -1
 R118308: 4 Sprobx0[10] + 3 Sproby0[10] - afterM0[9] - afterM0[10]
   - afterM0[11] - Fout0[9] + Fout0[10] - Fout0[11] >= 0
 R118309: 11 Sprobx0[10] + 7 Sproby0[10] - 3 afterM0[8] - afterM0[10]
   + afterM0[11] - 3 Fout0[8] - Fout0[9] - 2 Fout0[10] - 2 Fout0[11] >= 0
 R118310: 8 Sprobx0[10] + 4 Sproby0[10] - afterM0[9] - afterM0[10]
   - afterM0[11] - Fout0[8] - 2 Fout0[9] - Fout0[10] - Fout0[11] >= 0
 R118311: 4 Sprobx0[10] + 5 Sproby0[10] - 2 afterM0[8] + afterM0[9]
   - 2 afterM0[11] - Fout0[8] + 2 Fout0[9] - Fout0[11] >= 0
 R118312: 2 Sprobx0[10] + Sproby0[10] + afterM0[8] - afterM0[9]
   + afterM0[11] - Fout0[8] + Fout0[9] + 2 Fout0[10] - Fout0[11] >= 0
 R118313: Sprobx0[10] + 2 Sproby0[10] + afterM0[8] - afterM0[9]
   - afterM0[11] + Fout0[9] + Fout0[11] >= 0
 R118314: - Sprobx0[10] + afterM0[10] + Fout0[9] >= 0
 R118315: 4 Sprobx0[10] + 2 Sproby0[10] - 3 afterM0[9] + 2 Fout0[8]
   - Fout0[9] + Fout0[10] - Fout0[11] >= 0
 R118316: - 2 Sprobx0[10] - Sproby0[10] + afterM0[9] + 2 Fout0[8]
   + Fout0[9] + Fout0[11] >= 0
 R118317: Sproby0[10] - afterM0[8] - afterM0[9] + 2 afterM0[10] + Fout0[8]
   + 2 Fout0[10] >= 0
 R118318: 8 Sprobx0[10] + 4 Sproby0[10] + 2 afterM0[8] - 2 afterM0[9]
   - 2 afterM0[10] - 3 afterM0[11] - Fout0[9] + Fout0[10] - Fout0[11] >= 0
 R118319: 12 Sprobx0[10] + 7 Sproby0[10] - 3 afterM0[8] + afterM0[9]
   - afterM0[10] + afterM0[11] - 4 Fout0[8] - Fout0[9] - 2 Fout0[10]
   - 2 Fout0[11] >= 0
 R118320: 4 Sprobx0[10] + 2 Sproby0[10] + afterM0[8] + 2 afterM0[10]
   - Fout0[8] - 3 Fout0[9] - Fout0[10] >= 0
 R118321: - Sprobx0[10] + afterM0[9] + Fout0[8] >= 0
 R118322: Sprobx0[10] + 2 Sproby0[10] + 2 afterM0[8] + afterM0[9]
   + 2 afterM0[11] - Fout0[8] - Fout0[10] - Fout0[11] >= 0
 R118323: - Sprobx0[10] + afterM0[8] + afterM0[9] + afterM0[10] >= 0
 R118324: 4 Sprobx0[10] + 3 Sproby0[10] - afterM0[8] - afterM0[9]
   + afterM0[11] - Fout0[8] - 2 Fout0[9] + Fout0[10] + Fout0[11] >= 0
 R118325: Sprobx0[10] + 3 Sproby0[10] + afterM0[9] - afterM0[10]
   + afterM0[11] + Fout0[8] - Fout0[9] - Fout0[10] + Fout0[11] >= 0
 R118326: 4 Sprobx0[10] + 4 Sproby0[10] + afterM0[8] - afterM0[9]
   - 2 afterM0[10] - afterM0[11] + Fout0[8] - 2 Fout0[10] + 2 Fout0[11]
   >= 0
 R118327: 7 Sprobx0[10] + 4 Sproby0[10] - afterM0[8] + afterM0[9]
   - afterM0[10] + afterM0[11] - 4 Fout0[8] - Fout0[9] - Fout0[11] >= 0
 R118328: 12 Sprobx0[10] + 7 Sproby0[10] - 3 afterM0[8] - afterM0[9]
   - afterM0[10] - 2 afterM0[11] - 3 Fout0[8] - 2 Fout0[9] - Fout0[10]
   + 2 Fout0[11] >= 0
 R118329: - 2 Sprobx0[10] - Sproby0[10] + afterM0[9] + afterM0[10]
   + Fout0[8] + Fout0[9] >= 0
 R118330: 10 Sprobx0[10] + 2 Sproby0[10] + afterM0[8] - 3 afterM0[9]
   - 4 afterM0[10] - 2 afterM0[11] - Fout0[9] + 3 Fout0[10] + 3 Fout0[11]
   >= 0
 R118331: 4 Sprobx0[10] + Sproby0[10] + 2 afterM0[8] + 2 afterM0[9]
   - afterM0[10] + 4 afterM0[11] - 5 Fout0[8] - Fout0[9] + Fout0[10]
   + Fout0[11] >= 0
 R118332: 4 Sprobx0[10] + 2 Sproby0[10] - afterM0[8] - afterM0[9]
   - 3 afterM0[10] + afterM0[11] + 2 Fout0[9] + Fout0[11] >= 0
 R118333: - Sprobx0[11] - Sproby0[11] >= -1
 R118334: 4 Sprobx0[11] + 3 Sproby0[11] - afterM0[13] - afterM0[14]
   - afterM0[15] - Fout0[13] + Fout0[14] - Fout0[15] >= 0
 R118335: 11 Sprobx0[11] + 7 Sproby0[11] - 3 afterM0[12] - afterM0[14]
   + afterM0[15] - 3 Fout0[12] - Fout0[13] - 2 Fout0[14] - 2 Fout0[15]
   >= 0
 R118336: 8 Sprobx0[11] + 4 Sproby0[11] - afterM0[13] - afterM0[14]
   - afterM0[15] - Fout0[12] - 2 Fout0[13] - Fout0[14] - Fout0[15] >= 0
 R118337: 4 Sprobx0[11] + 5 Sproby0[11] - 2 afterM0[12] + afterM0[13]
   - 2 afterM0[15] - Fout0[12] + 2 Fout0[13] - Fout0[15] >= 0
 R118338: 2 Sprobx0[11] + Sproby0[11] + afterM0[12] - afterM0[13]
   + afterM0[15] - Fout0[12] + Fout0[13] + 2 Fout0[14] - Fout0[15] >= 0
 R118339: Sprobx0[11] + 2 Sproby0[11] + afterM0[12] - afterM0[13]
   - afterM0[15] + Fout0[13] + Fout0[15] >= 0
 R118340: - Sprobx0[11] + afterM0[14] + Fout0[13] >= 0
 R118341: 4 Sprobx0[11] + 2 Sproby0[11] - 3 afterM0[13] + 2 Fout0[12]
   - Fout0[13] + Fout0[14] - Fout0[15] >= 0
 R118342: - 2 Sprobx0[11] - Sproby0[11] + afterM0[13] + 2 Fout0[12]
   + Fout0[13] + Fout0[15] >= 0
 R118343: Sproby0[11] - afterM0[12] - afterM0[13] + 2 afterM0[14]
   + Fout0[12] + 2 Fout0[14] >= 0
 R118344: 8 Sprobx0[11] + 4 Sproby0[11] + 2 afterM0[12] - 2 afterM0[13]
   - 2 afterM0[14] - 3 afterM0[15] - Fout0[13] + Fout0[14] - Fout0[15]
   >= 0
 R118345: 12 Sprobx0[11] + 7 Sproby0[11] - 3 afterM0[12] + afterM0[13]
   - afterM0[14] + afterM0[15] - 4 Fout0[12] - Fout0[13] - 2 Fout0[14]
   - 2 Fout0[15] >= 0
 R118346: 4 Sprobx0[11] + 2 Sproby0[11] + afterM0[12] + 2 afterM0[14]
   - Fout0[12] - 3 Fout0[13] - Fout0[14] >= 0
 R118347: - Sprobx0[11] + afterM0[13] + Fout0[12] >= 0
 R118348: Sprobx0[11] + 2 Sproby0[11] + 2 afterM0[12] + afterM0[13]
   + 2 afterM0[15] - Fout0[12] - Fout0[14] - Fout0[15] >= 0
 R118349: - Sprobx0[11] + afterM0[12] + afterM0[13] + afterM0[14] >= 0
 R118350: 4 Sprobx0[11] + 3 Sproby0[11] - afterM0[12] - afterM0[13]
   + afterM0[15] - Fout0[12] - 2 Fout0[13] + Fout0[14] + Fout0[15] >= 0
 R118351: Sprobx0[11] + 3 Sproby0[11] + afterM0[13] - afterM0[14]
   + afterM0[15] + Fout0[12] - Fout0[13] - Fout0[14] + Fout0[15] >= 0
 R118352: 4 Sprobx0[11] + 4 Sproby0[11] + afterM0[12] - afterM0[13]
   - 2 afterM0[14] - afterM0[15] + Fout0[12] - 2 Fout0[14] + 2 Fout0[15]
   >= 0
 R118353: 7 Sprobx0[11] + 4 Sproby0[11] - afterM0[12] + afterM0[13]
   - afterM0[14] + afterM0[15] - 4 Fout0[12] - Fout0[13] - Fout0[15] >= 0
 R118354: 12 Sprobx0[11] + 7 Sproby0[11] - 3 afterM0[12] - afterM0[13]
   - afterM0[14] - 2 afterM0[15] - 3 Fout0[12] - 2 Fout0[13] - Fout0[14]
   + 2 Fout0[15] >= 0
 R118355: - 2 Sprobx0[11] - Sproby0[11] + afterM0[13] + afterM0[14]
   + Fout0[12] + Fout0[13] >= 0
 R118356: 10 Sprobx0[11] + 2 Sproby0[11] + afterM0[12] - 3 afterM0[13]
   - 4 afterM0[14] - 2 afterM0[15] - Fout0[13] + 3 Fout0[14] + 3 Fout0[15]
   >= 0
 R118357: 4 Sprobx0[11] + Sproby0[11] + 2 afterM0[12] + 2 afterM0[13]
   - afterM0[14] + 4 afterM0[15] - 5 Fout0[12] - Fout0[13] + Fout0[14]
   + Fout0[15] >= 0
 R118358: 4 Sprobx0[11] + 2 Sproby0[11] - afterM0[12] - afterM0[13]
   - 3 afterM0[14] + afterM0[15] + 2 Fout0[13] + Fout0[15] >= 0
 R118359: - Sprobx0[12] - Sproby0[12] >= -1
 R118360: 4 Sprobx0[12] + 3 Sproby0[12] - afterM0[17] - afterM0[18]
   - afterM0[19] - Fout0[17] + Fout0[18] - Fout0[19] >= 0
 R118361: 11 Sprobx0[12] + 7 Sproby0[12] - 3 afterM0[16] - afterM0[18]
   + afterM0[19] - 3 Fout0[16] - Fout0[17] - 2 Fout0[18] - 2 Fout0[19]
   >= 0
 R118362: 8 Sprobx0[12] + 4 Sproby0[12] - afterM0[17] - afterM0[18]
   - afterM0[19] - Fout0[16] - 2 Fout0[17] - Fout0[18] - Fout0[19] >= 0
 R118363: 4 Sprobx0[12] + 5 Sproby0[12] - 2 afterM0[16] + afterM0[17]
   - 2 afterM0[19] - Fout0[16] + 2 Fout0[17] - Fout0[19] >= 0
 R118364: 2 Sprobx0[12] + Sproby0[12] + afterM0[16] - afterM0[17]
   + afterM0[19] - Fout0[16] + Fout0[17] + 2 Fout0[18] - Fout0[19] >= 0
 R118365: Sprobx0[12] + 2 Sproby0[12] + afterM0[16] - afterM0[17]
   - afterM0[19] + Fout0[17] + Fout0[19] >= 0
 R118366: - Sprobx0[12] + afterM0[18] + Fout0[17] >= 0
 R118367: 4 Sprobx0[12] + 2 Sproby0[12] - 3 afterM0[17] + 2 Fout0[16]
   - Fout0[17] + Fout0[18] - Fout0[19] >= 0
 R118368: - 2 Sprobx0[12] - Sproby0[12] + afterM0[17] + 2 Fout0[16]
   + Fout0[17] + Fout0[19] >= 0
 R118369: Sproby0[12] - afterM0[16] - afterM0[17] + 2 afterM0[18]
   + Fout0[16] + 2 Fout0[18] >= 0
 R118370: 8 Sprobx0[12] + 4 Sproby0[12] + 2 afterM0[16] - 2 afterM0[17]
   - 2 afterM0[18] - 3 afterM0[19] - Fout0[17] + Fout0[18] - Fout0[19]
   >= 0
 R118371: 12 Sprobx0[12] + 7 Sproby0[12] - 3 afterM0[16] + afterM0[17]
   - afterM0[18] + afterM0[19] - 4 Fout0[16] - Fout0[17] - 2 Fout0[18]
   - 2 Fout0[19] >= 0
 R118372: 4 Sprobx0[12] + 2 Sproby0[12] + afterM0[16] + 2 afterM0[18]
   - Fout0[16] - 3 Fout0[17] - Fout0[18] >= 0
 R118373: - Sprobx0[12] + afterM0[17] + Fout0[16] >= 0
 R118374: Sprobx0[12] + 2 Sproby0[12] + 2 afterM0[16] + afterM0[17]
   + 2 afterM0[19] - Fout0[16] - Fout0[18] - Fout0[19] >= 0
 R118375: - Sprobx0[12] + afterM0[16] + afterM0[17] + afterM0[18] >= 0
 R118376: 4 Sprobx0[12] + 3 Sproby0[12] - afterM0[16] - afterM0[17]
   + afterM0[19] - Fout0[16] - 2 Fout0[17] + Fout0[18] + Fout0[19] >= 0
 R118377: Sprobx0[12] + 3 Sproby0[12] + afterM0[17] - afterM0[18]
   + afterM0[19] + Fout0[16] - Fout0[17] - Fout0[18] + Fout0[19] >= 0
 R118378: 4 Sprobx0[12] + 4 Sproby0[12] + afterM0[16] - afterM0[17]
   - 2 afterM0[18] - afterM0[19] + Fout0[16] - 2 Fout0[18] + 2 Fout0[19]
   >= 0
 R118379: 7 Sprobx0[12] + 4 Sproby0[12] - afterM0[16] + afterM0[17]
   - afterM0[18] + afterM0[19] - 4 Fout0[16] - Fout0[17] - Fout0[19] >= 0
 R118380: 12 Sprobx0[12] + 7 Sproby0[12] - 3 afterM0[16] - afterM0[17]
   - afterM0[18] - 2 afterM0[19] - 3 Fout0[16] - 2 Fout0[17] - Fout0[18]
   + 2 Fout0[19] >= 0
 R118381: - 2 Sprobx0[12] - Sproby0[12] + afterM0[17] + afterM0[18]
   + Fout0[16] + Fout0[17] >= 0
 R118382: 10 Sprobx0[12] + 2 Sproby0[12] + afterM0[16] - 3 afterM0[17]
   - 4 afterM0[18] - 2 afterM0[19] - Fout0[17] + 3 Fout0[18] + 3 Fout0[19]
   >= 0
 R118383: 4 Sprobx0[12] + Sproby0[12] + 2 afterM0[16] + 2 afterM0[17]
   - afterM0[18] + 4 afterM0[19] - 5 Fout0[16] - Fout0[17] + Fout0[18]
   + Fout0[19] >= 0
 R118384: 4 Sprobx0[12] + 2 Sproby0[12] - afterM0[16] - afterM0[17]
   - 3 afterM0[18] + afterM0[19] + 2 Fout0[17] + Fout0[19] >= 0
 R118385: - Sprobx0[13] - Sproby0[13] >= -1
 R118386: 4 Sprobx0[13] + 3 Sproby0[13] - afterM0[21] - afterM0[22]
   - afterM0[23] - Fout0[21] + Fout0[22] - Fout0[23] >= 0
 R118387: 11 Sprobx0[13] + 7 Sproby0[13] - 3 afterM0[20] - afterM0[22]
   + afterM0[23] - 3 Fout0[20] - Fout0[21] - 2 Fout0[22] - 2 Fout0[23]
   >= 0
 R118388: 8 Sprobx0[13] + 4 Sproby0[13] - afterM0[21] - afterM0[22]
   - afterM0[23] - Fout0[20] - 2 Fout0[21] - Fout0[22] - Fout0[23] >= 0
 R118389: 4 Sprobx0[13] + 5 Sproby0[13] - 2 afterM0[20] + afterM0[21]
   - 2 afterM0[23] - Fout0[20] + 2 Fout0[21] - Fout0[23] >= 0
 R118390: 2 Sprobx0[13] + Sproby0[13] + afterM0[20] - afterM0[21]
   + afterM0[23] - Fout0[20] + Fout0[21] + 2 Fout0[22] - Fout0[23] >= 0
 R118391: Sprobx0[13] + 2 Sproby0[13] + afterM0[20] - afterM0[21]
   - afterM0[23] + Fout0[21] + Fout0[23] >= 0
 R118392: - Sprobx0[13] + afterM0[22] + Fout0[21] >= 0
 R118393: 4 Sprobx0[13] + 2 Sproby0[13] - 3 afterM0[21] + 2 Fout0[20]
   - Fout0[21] + Fout0[22] - Fout0[23] >= 0
 R118394: - 2 Sprobx0[13] - Sproby0[13] + afterM0[21] + 2 Fout0[20]
   + Fout0[21] + Fout0[23] >= 0
 R118395: Sproby0[13] - afterM0[20] - afterM0[21] + 2 afterM0[22]
   + Fout0[20] + 2 Fout0[22] >= 0
 R118396: 8 Sprobx0[13] + 4 Sproby0[13] + 2 