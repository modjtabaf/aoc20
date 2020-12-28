
(if #t
(define input (list
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
))
(define input (list
77
10
143
46
79
97
54
116
60
91
80
132
20
154
53
14
103
31
65
110
43
38
47
120
112
87
24
95
33
104
73
22
66
137
21
109
118
63
55
124
146
148
84
86
147
125
23
85
117
71
48
136
151
130
83
56
140
9
49
113
131
133
74
37
127
34
32
106
1
78
11
72
40
96
17
64
92
102
123
126
90
105
57
99
27
70
98
111
30
50
67
2
155
5
119
8
39
))
)

(set! input (cons 0 input))

(set! input (sort input (lambda (a b) (< a b))))

(define diffs (map (lambda (p) (- (car p) (cadr p))) (zip (cdr input) input)))
(pp diffs)

(define num1s 0)
(define num3s 1)

(for-each
  (lambda (n)
    (if (= n 1)
      (set! num1s (1+ num1s))
      (if (= n 3)
        (set! num3s (1+ num3s))
      )
    )
  )
  diffs
)

(pp (list num1s num3s (* num1s num3s)))
