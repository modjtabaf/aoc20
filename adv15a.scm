
(if #f
(define input (list
0 3 6
))
(define input (list
20 9 11 0 1 2
))
)

(define spokens '())

(define (next-number spoken turn) (let
  (
    (next)
    (foo)
  )
  ;(pp spoken)
  (set! foo (assoc spoken spokens))
  (if foo (begin
    (set! next (- (cadr foo) (cddr foo)))
    ;(pp next)
    (set! foo (assoc next spokens))
    ;(pp foo)
    (if foo
      (set-cdr! foo (cons turn (cadr foo)))
    (begin
      (set! foo (cons next (cons turn turn)))
      (set! spokens (cons foo spokens))
    ))
  ) (begin
    (set! foo (cons spoken (cons turn turn)))
    (set! spokens (cons foo spokens))
  ))
  foo
))

(define turn 0)
(define spoken)

(for-each
  (lambda (n)
    (set! spoken (car (next-number n turn)))
    (set! turn (1+ turn))
  )
  input
)

(do
  ((k (length input) (1+ k)))
  ((>= k 2020))
  (set! spoken (car (next-number spoken k)))
  (pp spoken)
)

(pp spoken)
