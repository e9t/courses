Title: Introduction to Python
Date: 2015-03-08 18:00
Toc: True


## 들어가기 전에

1. 운영체제(OS)란?
    - ["시스템 하드웨어와 소프트웨어를 실행하기 위한 시스템 소프트웨어"](http://ko.wikipedia.org/wiki/%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C)
        - ex: 윈도우 7, Mac OS 10.10, Ubuntu 14.04, iOS 6, Android 5.0, ...
    - 프로그래밍을 하기 전에는 내가 어떤 OS의 어떤 버젼을 사용하고 있는지 꼭 알아두자!
    - **여기서는 윈도우 7을 사용하고 있다는 가정 하에 튜토리얼을 진행합니다.**
1. 쉘(shell)이란?
    - ["운영체제 상에서 다양한 운영체제 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램"](http://ko.wikipedia.org/wiki/%EC%85%B8)
    - 운영체제의 핵심 부분을 구성하는 "커널(kernel)"을 감싸고 있다는 뜻에서 "쉘"이라는 이름이 붙었죠<br>
    <a href="http://www.quora.com/What-is-the-origin-of-the-name-shell"><img src="images/kernel.gif" width="250px"></a>

## 왜 파이썬인가?

1. Python is now the most popular introductory language at Top US Universities (July, 2014)<br>
<a href="http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext"><img src="images/python.png" width="400px"></a>
1. Python is a major programming language for data mining (Aug, 2014)<br>
<a href="http://www.kdnuggets.com/2014/08/four-main-languages-analytics-data-mining-data-science.html"><img src="images/kdnuggets.jpg" width="350px"></a>

So is Python the best programming language ever?

- No, and [there probably will never be such a thing](http://paulgraham.com/hundred.html)
- But, definitely worth the effort for now

그렇다면 진짜로 왜?

1. 쉽다
1. 간편하다

...외에도 가독성(readability)이 좋다는 점, 문서화(documentation)가 잘 되어있다는 점, 라이브러리/패키지가 풍부해서 데이터 분석부터 시각화, 웹프로그래밍 등 다양한 영역에 사용할 수 있다는 점, 개발 커뮤니티가 활발하다는 점 등 때문에 [처음 배우는 프로그래밍 언어로써](http://blog.trinket.io/why-python/), 그리고 [연구용 언어로써](http://www.stat.washington.edu/~hoytak/blog/whypython.html) 좋다는 평가가 있습니다.

> 파이썬 프로그래밍을 하다가 궁금한 점이 있을 때는 아래 커뮤니티들에 질문을 던져보세요:<br>
> 1. [파이썬 코리아 페이스북 그룹](https://www.facebook.com/groups/pythonkorea/)<br>
> 2. [생활코딩 페이스북 그룹](https://www.facebook.com/groups/codingeverybody/)<br>
> 그 외에도 [파이조그(PyJog)](https://www.facebook.com/pyjog)와 같이 주말에 오프라인으로 모여서 각자 코딩하는 모임도 있습니다. 고수님들을 만날 기회이니 프로그래밍을 더 잘해보고 싶은 분은 한 번쯤 참석해보시기 바랍니다.


## Installing Python

- 윈도우에서 자바 프로그래밍 환경을 마련하는 일반적인 절차는?
    - 1단계: [자바 개발 키트 (JDK)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) 설치 (2015년 3월 현재, JDK 8u40 배포중)
    - 2단계: 환경변수 설정 (ex: `JAVA_HOME`)
    - 3단계: 자바 IDE 설치 (ex: [이클립스](https://eclipse.org/), [IntelliJ IDEA](https://www.jetbrains.com/idea/))
- 윈도우에서 R 프로그래밍 환경을 마련하는 일반적인 절차는?
    - 1단계: [R 배포판](http://cran.r-project.org/) 설치 (2015년 3월 현재, R 3.1.2 배포중)
    - 2단계: R IDE 설치 (ex: [RStudio](http://rstudio.com))
- 윈도우에서 파이썬 프로그래밍 환경을 마련하는 일반적인 절차는?
    - 1단계: [파이썬 배포판](http://python.org/download) 설치
    - 2단계: 파이썬 IDE 설치

자, 그럼 시작해봅시다!

### 1단계: 파이썬 배포판 설치

1. Download [Continuum's Anaconda](http://continuum.io/downloads#34)
    - 잠깐, [python.com](http://python.org/download)이 아니라 딴데서 설치파일을 다운받으라고?
        - python.com/download: 파이썬 정식 배포판
        - continuum.io/downloads#34: 파이썬 사제 배포판<br>
    <img src="images/anaconda.png" width="600px">
    - 파이썬 정식 배포판이 아니라 일반 회사의 사제 배포판을 사용하는 이유는?
        - Windows에서는 파이썬의 몇몇 패키지 설치가 어렵다는 풍문이 있다
        - 이를 극복하기 위해 [윈도우만을 위해 사전에 컴파일 된 패키지를 따로 제공하는 사람도 있다](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
        - 우리는 패키지 설치의 번거로움에서 벗어나기 위해 사전에 [195개의 패키지](http://docs.continuum.io/anaconda/pkg-docs.html)가 한꺼번에 깔리는 배포판을 선택
    - [Python 2 vs Python 3](https://wiki.python.org/moin/Python2orPython3)
        - 아직까지 학계에서는 Python 2도 많이 사용
        - 하지만 우리는 더 최신 버젼인 Python 3 선택
            1. 파이썬 3가 유니코드 서포트를 해서 한국어를 사용하는 사람들에게 편리
            2. 파이썬 3 is [the way to go](http://pythonkr.github.io/pyconkr-2014/pdf/pyconkr-2014-25_geofront.pdf)
            3. [이제 많은 라이브러리들이 파이썬 3도 지원](http://python3wos.appspot.com/)
2. Install Anaconda
    - 환경변수 설정은 아나콘다가 알아서 해줌<br>
    <img src="images/anaconda2.png" width="400px">
3. Run Python!
    - 콘솔을 열어 `ipython`을 입력해서 파이썬 쉘을 열어보자.
    - 파이썬 쉘이 열리면:

            :::python
            >>> print("Hello world!")
            Hello world!
            >>> 1+3
            4
            >>> 1/3
            0.3333333333333333
            >>> 2**10
            1024

    - Now you're a Python programmer! (적어도 계산기로는 쓸 수 있다)

### 2단계: 파이썬 IDE 설치
위와 같이 파이썬을 쉘(shell)에서 실행하는 방법도 있지만,
스크립트(script) 파일을 이용해서 파이썬을 실행할 수도 있다.

쉘은 순간적인 실행을 위해서는 아주 편리하지만,
긴 프로그램을 짜고자 할 때, 또는 프로그램을 저장하고자 할 때는 적합하지 않다.

이를 위해 다음의 몇 가지 절차를 거치면 파일을 이용해 파이썬 스크립트를 실행할 수 있다.

1. 윈도우에서 메모장을 열고
2. 다음의 헬로월드 출력문을 파일에 입력한 후 (또는 다른 파이썬 코드를 입력해도 좋다)

        print("Hello world!")
        print("Hello world full of data!")
        print("데이터마이닝을 위한 파이썬!")

3. 파일을 바탕화면에 `test.py`라는 이름으로 저장하자.
4. 마지막으로, 콘솔을 열어 아래와 같이 입력하면 파이썬 파일이 실행된다. 첫번째 줄은 윈도우 탐색기에서 "바탕화면"으로 이동하라는 버튼을 누른 것과 같고, 두번째 줄은 윈도우 탐색기에서 `test.py` 파일을 클릭하여 실행한 것과 같다. 멋지지 않은가? 이제 우리도 GUI(graphic user interface)가 아니라 CLI(command line interface)에서 프로그래밍을 할 수 있게 된 것이다!

        cd ~/Desktop
        python test.py

    연습삼아, `test.py`의 내용을 바꿔가며 아래의 다양한 예시를 입력해보자.
    각 예시는 이해를 돕기 위해 자바 1.7과 병렬적으로 배치해두었다.

#### 예시 1: "Hello world"

프로그래밍의 기본! Hello world를 출력해보자.
자바와 파이썬 코드에 어떤 차이점이 있는가?

1. 먼저 자바 코드와는 달리 파이썬 코드에서는 `public class MyClass { ... }` 등과 같이 클래스를 선언하지 않아도 된다.
1. `public static void main (String[] args) { ... }` 등과 같이 복잡하게 메인함수를 선언하지 않아도 된다.
1. 세미콜론(;)을 붙이지 않아도 된다.

그리하여 파이썬으로는 무려 한 줄 만으로도 Hello world를 출력할 수 있다.

- Java 1.7

        :::java
        public class MyClass {
            public static void main (String[] args) {
                System.out.println("Hello world");
            }
        }

- Python 3

        :::python
        print("Hello world")

#### 예시 2: 변수 선언

변수를 선언해보자.
아래 코드에서는 앞서 언급된 차이점들 외에도 크게 두 가지 차이점을 발견할 수 있다.

1. 파이썬에서는 변수의 데이터 타입(type), 즉 String인지 int인지 등을 선언할 필요가 없다.이를 동적 타이핑(dynamic typing)이라고 하는데, 이는 변수의 데이터 타입이 고정되어 있지 않고 변할 수 있다는 말이다. 반면 자바에서는 변수의 데이터 타입을 미리 지정해줘야하고 한 번 지정하고 나면 변수의 타입은 바뀔 수 없다. 
2. 자바 코드에서는 변수를 선언할 때 `myString`과 같이 [camelCase](http://en.wikipedia.org/wiki/CamelCase)를 사용하는데 반해 파이썬 코드에서는 `my_string`과 같이 [underscore](http://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby)를 사용한다. 파이썬의 스타일링에 관해서는 [PEP-8](https://www.python.org/dev/peps/pep-0008/)에 잘 나와 있다. 이 문서를 지금 당장 다 읽지 않더라도, 중요한 지침을 담고 있으니 반드시 이름은 기억해두자.

- Java 1.7 (static typed)

        :::java
        String myString = "this is a string";

- Python 3 (dynamic typed)

        :::python
        my_string = "this is a string"

#### 예시 3: 파일 쓰기 (writing)

아래는 `some_file.txt`에 "Hello world full of data!"라는 문자열을 입력하는 코드이다.
자바에서 파일 입출력(I/O)은 생각만큼 간단하지 않지만, 파이썬에서는 코드도 무척 간단하게 읽힌다.
이렇게 읽으면 된다: `"some_file.txt"`를 `"w(write)"`모드로 읽어서, 그것을 `f`라고 부르자.
그리고 `f`에는 `"Hello world full of data!"`라는 문자열을 쓰자(`write`)!

- Java 1.7

        :::java
        import java.io.*;
        
        public class WriteFile {
            public static void main(String[] args) throws IOException {
                Writer writer = null;
                try {
                    writer = new BufferedWriter(new OutputStreamWriter(
                          new FileOutputStream("some_file.txt"), "utf-8"));
                    writer.write("Hello world full of data!");
                } catch (IOException ex) {
                    System.out.println("An exception occurred during writing file.");
                } finally {
                    try {writer.close();} catch (Exception ex) {}
                }
            }
        }

- Python 3

        :::python
        with open("some_file.txt", "w") as f:
            f.write("Hello world full of data!")

#### 예시 4: 파일 읽기 (reading)

이미 바탕화면에는 `some_file.txt`라는 파일이 생겼을 것이다. 한 번 확인해보자.
만일 `test.py` 파일을 바탕화면이 아니라 다른 폴더 안에 저장했다면, `some_file.txt`는 그 폴더 안에 있을 것이다.

이번에는 그 파일의 내용을 읽어보자.
아마도 "Hello world full of data!"가 출력되겠지?

- Java 1.7

        :::java
        import java.io.BufferedReader;
        import java.io.FileReader;
        import java.io.IOException;
        
        public class ReadFile {
            public static void main(String[] args) throws IOException {
                BufferedReader br = new BufferedReader(new FileReader("some_file.txt"));
                try {
                    StringBuilder sb = new StringBuilder();
                    String line = br.readLine();
        
                    while (line != null) {
                        sb.append(line);
                        sb.append(System.lineSeparator());
                        line = br.readLine();
                    }
                    String everything = sb.toString();
                    System.out.println(everything);
                } finally {
                    br.close();
                }   
            }
        }

- Python 3

        :::python
        with open("some_file.txt", "r") as f:
            d = f.read()
        print d



#### 예시 5: 클래스(class)와 상속(inheritance)

예시 1에서도 설명했지만, 파이썬에서는 클래스를 반드시 선언해주지는 않아도 된다.
하지만, 클래스가 유용한 경우는 종종 있고, 파이썬에서도 클래스를 만들 수 있다.
아래 코드를 참고하자.

- Java 1.7

        :::java
        class Animal {
            protected String name;
            public Animal(String name) {
                this.name = name;
            }   
            public void saySomething() {
                System.out.println("I am a " + name + ".");
            }   
        }   

        class Dog extends Animal {
            public Dog(String name) {
                super(name);
            }   
            public void saySomething() {
                System.out.println("I am a " + name + ". Bark, bark!");
            }   
        }   

        public class ClassTest {
            public static void main(String[] args) {
                Dog dog = new Dog("Chiwawa");
                dog.saySomething();
            }   
        } 

- Python 3

        :::python
        class Animal():

            def say_something(self):
            print "I am a " + self.name + "."

            def __init__(self, name):
                self.name = name

        class Dog(Animal):
            def say_something(self):
                print "I am a " + self.name + ". Bark, bark!"

        dog = Dog("Chiwawa")
        dog.say_something()

## Appendix

### 초짜 프로그래머가 프로그래밍 잘하는 법
1. 에러 메세지를 잘 *읽자* (read, not see). 흔히들 시험 볼 때 문제 속에 답이 있다고 하는데, 프로그래밍할 때는 에러 메세지 속에 이유가 있다. 진짜다.
1. 좋은 레퍼런스 찾기
    1. 공식 문서 (official documents) / API 보기 (ex: [docs.python.org](http://docs.python.org))
    2. [구글링!](http://lmgtfy.com/?q=python docs) (주의: 구글링을 한다고 무조건 좋은 레퍼런스가 찾아지는 것은 아니다)
1. Learning how to program, rather than just accomplishing the task
    - 프로그래밍을 배우는 것과 복/붙하는 것은 다르다 (참고: [Teach yourself programming in ten years](http://norvig.com/21-days.html))
    - 일단 프로그램이 작동하게 하는데 성공했다면, 왜 작동했는지를 이해하지
1. Follow coding conventions. 많은 똑똑한 사람들이 선택한 방법에는 이유가 있다.
    - [PEP-8](https://www.python.org/dev/peps/pep-0008)

### 윈도우 프로그래머를 위한 팁

1. 윈도우에서 자주 속썩이는 것들
    1. 인코딩이 골치. UTF8 쓰는게 OS간 호환성에 가장 좋지만, 윈도우는 EUC-KR이 기본. 한글 사용자라면 [유니코드가 뭔지 알고 가자](http://www.joelonsoftware.com/articles/Unicode.html).
    1. Newlines가 골치. (참고: http://blog.codinghorror.com/the-great-newline-schism/, http://en.wikipedia.org/wiki/Newline)
    1. 역슬래시가 골치
        - 왜 내 키보드에는 역슬래시가 없을까? (폰트 문제)
        - 폴더 구분자를 쓸 때 왜 역슬래시를 두 번 표기해야할까?
        - 폴더 구분자를 쓸 때 왜 역슬래시 대신 슬래시를 쓸까?
    1. 사용자(user)의 홈디렉토리(home directory)에 대한 개념을 익히자
        - 보통 사용자가 "lucypark"라면 윈도우에서 홈디렉토리는 `C:\Users\lucypark`. 맥이나 리눅스에서는 `~/`
        - 다른 OS를 한번쯤 써보면 금세 익힐 수 있게 된다!
    1. 탐색기(Explorer) 설정 변경<br>
    <img src="images/windows.png" width="700px">

    "파일 확장명 숨기기" 선택 해제를 하고 나면 다음과 같이 된다.
    파일이 확장자(extension)가 있는지, 없는지, 있다면 어떤 확장자인지 아는 것은 중요하다.
    확장자는 우리가, 그리고 컴퓨터가, 파일이 어떤 프로그램으로 실행할 수 있는지 알 수 있는 힌트이기 때문이다.

    <img src="images/windows2.png" width="700px">

### 그 밖의 유용한 참고자료

- 최성철, [산업공학과를 위한 프로그래밍 입문 (w/파이썬) Part 1: 파이썬 기초](http://www.slideshare.net/blissray/w-37771905), 2014.
- 최성철, [산업공학과를 위한 프로그래밍 입문 (w/파이썬) Part 2: 파이썬 활용](http://www.slideshare.net/blissray/w-part-2), 2014.
