#importpyas "sample.py" ""

(define testdata 12)

(define (make-stream next init)
  (list (lambda (x)
          (local [(define curnum init)]
            ((lambda (x) curnum) x)))
        next init))

(define (stream-get stream)
  (local
    [(define current (first stream))
     (define init (third stream))]
    (current init)))

(define (stream-next stream)
  (local [(define current (first stream))
          (define next (second stream))
          (define init (third stream))]
  (list (lambda (x)
          (local [(define curnum (current init))]
            ((lambda (x) (next curnum)) x)))
        next init)))

(define (stream-reset stream)
  (local [(define next (second stream))
          (define init (third stream))]
    (list (lambda (x)
          (local [(define curnum init)]
            ((lambda (x) curnum) x)))
        next init)))

(define (stream-gen stream n)
  (cond [(zero? n) empty]
        [else (cons (stream-get stream)
                    (stream-gen (stream-next stream)
                                (sub1 n)))]))
