import sys
import InputMultiGene
import pandas as pd
import numpy as np

"""
Problem Title: Consensus and Profile
URL: http://rosalind.info/problems/cons/
DataSet: rosalind_cons.txt
Result: result_cons.txt

Example
-------
$ python Consensus_and_profile.py rosalind_cons.txt > result_cons.txt
"""


class StringDataFrame(object):
    """
    Attributes
    ----------
    StringDataframe : pandas.core.frame.DataFrame
        行方向に配列を格納したPandasデータフレーム。行インデックスに配列名を取る。
        その一方、列インデックスはサイトだが0からのスタートになってしまっている点は注意。
    ProfileDataframe : pandas.core.frame.DataFrame
        コンセンサス配列に関するデータを格納するデータフレーム。行インデックスはA, C, G, Tの順に塩基をとる。
        その一方、列インデックスはサイトだが0からのスタートになってしまっている点は注意。
        格納されているデータは、StringDataframeにおいて、(i+1)番目のサイトにある塩基が存在する配列の数を示す。
        ex)7列目のCの行が5だった場合、配列の(7+1)=8文字目にCが存在する配列が5本ある。

    """

    def __init__(self):
        self.StringDataframe = pd.DataFrame() # DataFrame of DNA Strings
        self.ProfileDataframe = pd.DataFrame(dtype='i8') # DataFrame of Profile
        self.ConsensusString = "" 
        

    def ImportDnaDict(self, dict):
        """
        { 配列名 : 配列 }という辞書型のデータを受け取り、Pandasのデータフレーム形式に変換する。

        Parameters
        ----------
        dict : 辞書型
            { 配列名 : 配列 }という形式になっている。

        Returns
        -------
        self.StringDataframe : pandas.core.frame.DataFrame
            行方向に配列を格納したPandasデータフレーム。行インデックスに配列名を取る。
            その一方、列インデックスはサイトだが0からのスタートになってしまっている点は注意。
        """
        for name, sequence in dict.items():
            tmp_df = pd.DataFrame([list(sequence)], index=[name])
            self.StringDataframe = self.StringDataframe.append(tmp_df)

        return self.StringDataframe
    
    def ProfileMatrix(self):
        """
        StringDataframeからProfileDataframeを作成する。

        Returns
        -------
        ProfileDataframe : pandas.core.frame.DataFrame
        コンセンサス配列に関するデータを格納するデータフレーム。行インデックスはA, C, G, Tの順に塩基をとる。
        その一方、列インデックスはサイトだが0からのスタートになってしまっている点は注意。
        格納されているデータは、StringDataframeにおいて、(i+1)番目のサイトにある塩基が存在する配列の数を示す。
        ex)7列目のCの行が5だった場合、配列の(7+1)=8文字目にCが存在する配列が5本ある。
        """

        for i in range(0, len(self.StringDataframe.columns)):
            record = self.StringDataframe[i].value_counts() # 
            self.ProfileDataframe = pd.concat([self.ProfileDataframe, record], axis=1)
            
        self.ProfileDataframe = self.ProfileDataframe.fillna(0) # 欠損値NaNを0に置換(この時dtypeはfloat64になる)
        self.ProfileDataframe = self.ProfileDataframe.astype(int) # dtypeをfloat64->intに変換して返り値とする

        return self.ProfileDataframe 

    def CreateConsensusString(self):
        self.ModeSereies = self.StringDataframe.mode()
        for i in range(0, len(self.ModeSereies.columns)):
            self.ConsensusString += self.ModeSereies.iat[0, i]
        return self.ConsensusString
        

def main():
    dna_dict = InputMultiGene.InputMultiGene().input_multi_gene(sys.argv[1])
    
    sdf = StringDataFrame()
    sdf.ImportDnaDict(dna_dict)

    profile = sdf.ProfileMatrix()
    result = profile.T.to_dict(orient='list')
    
    print(sdf.CreateConsensusString())
    for symbol, sequence in result.items():
        print(symbol + ":", " ".join( map(str, sequence) ))

    
    
if __name__ == "__main__":
    main()