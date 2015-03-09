Title: 파이썬 프로그래밍을 위한 Sublime Text
Date: 2015-03-09 13:26
Toc: True

## Installation

1. Sublime Text 설치<br>
[![sublime](images/sublime.png)](http://sublimetext.com)
2. [Sublime Text 패키지 매니저](https://packagecontrol.io/installation#st2) 설치

> 내가 설치한 Sublime Text의 버젼을 잘 확인하자! 2인가 3인가?

## Troubleshooting

### 파이썬 build 시 한글 출력문에 `[Decode error - output not utf-8]`가 출력되는 문제

1. 콘솔에서 `chcp`를 입력하여 윈도우 코드 페이지(codepage) 확인 (아마도 949일 것)
2. `C:\Users\lucypark\AppData\Roaming\Sublime Text 2\Packages\Python\Python.sublime-build` 파일을 열어 아래의 마지막 줄 추가 입력 (바로 직전의 `,`도 빼먹지 말 것!)

        {
            "cmd": ["python", "-u", "$file"],
            "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
            "selector": "source.python",
            "encoding": "cp949"
        }

## Suggested packages

### IMESupport: 한글 입력이 한 박자 늦게 되는 문제 해결

- [**IMESupport** 패키지 설치](http://meaningone.tistory.com/116)

### Origami: Divide window to several panes

- 방법 1.<br>
<img src="images/pane.png" width="500px">
- 방법 2. Install the **Origami** package (훨씬 다양하게 pane을 나눠 쓸 수 있음)

### SublimeREPL: Python REPL in Sublime

<img src="images/repl.png" width="500px">
