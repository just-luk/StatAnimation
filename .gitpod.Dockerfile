FROM gitpod/workspace-base

RUN sudo install-packages ffmpeg libcairo2-dev libpango1.0-dev
RUN pip install manim
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
RUN export PATH=$PATH:~/bin
RUN tlmgr install collection-basic amsmath babel-english cbfonts-fd cm-super ctex doublestroke dvisvgm everysel fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin mathastext microtype ms physics preview ragged2e relsize rsfs setspace standalone tipa wasy wasysym xcolor xetex xkeyval
RUN tlmgr path add
