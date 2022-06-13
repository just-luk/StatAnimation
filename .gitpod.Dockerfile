FROM gitpod/workspace-full

RUN sudo install-packages ffmpeg libcairo2-dev libpango1.0-dev
RUN pip install manim
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
