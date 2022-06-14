FROM gitpod/workspace-full

RUN sudo install-packages ffmpeg libcairo2-dev libpango1.0-dev
RUN pip install manim moviepy pydub
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
RUN ~/bin/tlmgr install collection-basic amsmath babel-english cbfonts-fd cm-super ctex doublestroke dvisvgm everysel fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin mathastext microtype ms physics preview ragged2e relsize rsfs setspace standalone tipa wasy wasysym xcolor xetex xkeyval
RUN ~/bin/tlmgr path add
ENV PATH="~/bin:${PATH}" 
