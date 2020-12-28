
(if #f
(define input (list
939
7 13 0 0 59 0 31 19
))
(define input (list
1000511
29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 37 0 0 0 0 0 409 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 17 13 19 0 0 0 23 0 0 0 0 0 0 0 353 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 41
))
)

(define dep-time (car input))
(set! input (cdr input))
(define earliest-t '())
(define earliest-id '())

(for-each
  (lambda (id)
    (if (> id 0) (let
      (
        (t (* (ceiling (/ dep-time id)) id))
      )
      
      (if (or (null? earliest-t) (< t earliest-t)) (begin
        (set! earliest-t t)
        (set! earliest-id id)
      ))
    ))
  )
  input
)

(pp (list earliest-t earliest-id (* (- earliest-t dep-time) earliest-id)))
