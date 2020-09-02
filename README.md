# cpp-auto-bundle
c++の#include"hoge"を展開します

# インストール
bundle.pyを何らかの方法でカレントディレクトリにコピー

# 使い方
python3をいれる
```
./bundle.py <cppファイルのPATH>
```
で標準出力に展開されたコードが出力されるので
```
./bundle.py ./main.cpp >./output.cpp
```
等をしてフォルダ出力する

# 注意
1時間クオリティなので色々ミスがあるかも
