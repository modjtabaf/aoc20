
(if #f
(define input (list
(cons 'nop +0)
(cons 'acc +1)
(cons 'jmp +4)
(cons 'acc +3)
(cons 'jmp -3)
(cons 'acc -99)
(cons 'acc +1)
(cons 'jmp -4)
(cons 'acc +6)
))
(define input (list
(cons 'acc -17)
(cons 'nop +318)
(cons 'jmp +1)
(cons 'acc -10)
(cons 'jmp +394)
(cons 'acc +43)
(cons 'acc +47)
(cons 'nop +570)
(cons 'jmp +176)
(cons 'acc -9)
(cons 'jmp +322)
(cons 'jmp +73)
(cons 'acc +4)
(cons 'acc -4)
(cons 'jmp +460)
(cons 'jmp +228)
(cons 'acc +25)
(cons 'acc +39)
(cons 'jmp +50)
(cons 'acc -12)
(cons 'acc -14)
(cons 'nop +275)
(cons 'jmp +489)
(cons 'acc -11)
(cons 'jmp +338)
(cons 'acc +21)
(cons 'acc +10)
(cons 'jmp +1)
(cons 'acc +20)
(cons 'jmp +445)
(cons 'acc +7)
(cons 'jmp +419)
(cons 'acc -8)
(cons 'acc +32)
(cons 'jmp +181)
(cons 'acc +19)
(cons 'acc +5)
(cons 'acc +46)
(cons 'jmp +417)
(cons 'acc +28)
(cons 'acc +23)
(cons 'acc +16)
(cons 'jmp +225)
(cons 'jmp +317)
(cons 'jmp +309)
(cons 'jmp +69)
(cons 'acc -6)
(cons 'acc -6)
(cons 'jmp +127)
(cons 'acc +49)
(cons 'nop -38)
(cons 'jmp +467)
(cons 'acc +0)
(cons 'acc -12)
(cons 'acc -14)
(cons 'jmp -46)
(cons 'acc +14)
(cons 'acc +2)
(cons 'acc +2)
(cons 'jmp +311)
(cons 'acc +33)
(cons 'jmp +364)
(cons 'nop +234)
(cons 'acc +24)
(cons 'acc +37)
(cons 'acc +18)
(cons 'jmp +22)
(cons 'jmp +303)
(cons 'jmp +414)
(cons 'jmp +318)
(cons 'acc +22)
(cons 'acc +27)
(cons 'jmp +1)
(cons 'jmp +150)
(cons 'acc +34)
(cons 'acc +15)
(cons 'nop +200)
(cons 'acc +6)
(cons 'jmp +320)
(cons 'nop +534)
(cons 'acc +29)
(cons 'jmp +147)
(cons 'nop -20)
(cons 'jmp +255)
(cons 'jmp +10)
(cons 'acc -15)
(cons 'acc +3)
(cons 'jmp +338)
(cons 'nop +362)
(cons 'acc -4)
(cons 'jmp +1)
(cons 'jmp +286)
(cons 'acc -1)
(cons 'jmp +497)
(cons 'acc -4)
(cons 'acc +23)
(cons 'acc +4)
(cons 'jmp +400)
(cons 'acc +35)
(cons 'acc +50)
(cons 'jmp +133)
(cons 'acc -17)
(cons 'jmp -90)
(cons 'jmp +7)
(cons 'acc -17)
(cons 'jmp +472)
(cons 'acc +20)
(cons 'jmp +280)
(cons 'jmp +133)
(cons 'jmp -15)
(cons 'jmp +16)
(cons 'acc -19)
(cons 'acc -2)
(cons 'jmp -64)
(cons 'acc -17)
(cons 'jmp +1)
(cons 'jmp +385)
(cons 'acc -5)
(cons 'acc +34)
(cons 'jmp +382)
(cons 'acc +24)
(cons 'acc -17)
(cons 'acc +0)
(cons 'acc +15)
(cons 'jmp +466)
(cons 'jmp +300)
(cons 'acc +16)
(cons 'jmp +302)
(cons 'nop +479)
(cons 'acc +16)
(cons 'jmp +71)
(cons 'acc +23)
(cons 'jmp +1)
(cons 'acc +8)
(cons 'jmp +154)
(cons 'jmp +410)
(cons 'acc -8)
(cons 'jmp +402)
(cons 'acc +48)
(cons 'acc +42)
(cons 'acc +22)
(cons 'acc +35)
(cons 'jmp +50)
(cons 'jmp -7)
(cons 'acc -13)
(cons 'acc +37)
(cons 'acc +24)
(cons 'jmp +243)
(cons 'jmp +410)
(cons 'acc -3)
(cons 'acc +45)
(cons 'jmp +416)
(cons 'acc +2)
(cons 'acc +25)
(cons 'jmp -109)
(cons 'jmp -41)
(cons 'jmp +318)
(cons 'acc -8)
(cons 'acc -12)
(cons 'jmp +169)
(cons 'nop +393)
(cons 'acc +7)
(cons 'acc -12)
(cons 'acc +35)
(cons 'jmp +381)
(cons 'acc +41)
(cons 'nop -98)
(cons 'acc +15)
(cons 'acc -19)
(cons 'jmp +218)
(cons 'acc +24)
(cons 'acc +47)
(cons 'jmp +65)
(cons 'acc +29)
(cons 'jmp -129)
(cons 'acc +23)
(cons 'acc -13)
(cons 'nop +60)
(cons 'jmp -26)
(cons 'nop -4)
(cons 'acc -5)
(cons 'acc +13)
(cons 'nop -12)
(cons 'jmp -13)
(cons 'jmp -53)
(cons 'acc +21)
(cons 'jmp +276)
(cons 'nop -27)
(cons 'jmp +165)
(cons 'acc +42)
(cons 'nop +43)
(cons 'jmp +1)
(cons 'acc +26)
(cons 'acc +22)
(cons 'acc -3)
(cons 'jmp +405)
(cons 'acc +29)
(cons 'nop -118)
(cons 'acc +21)
(cons 'nop -190)
(cons 'jmp +217)
(cons 'acc -1)
(cons 'nop +223)
(cons 'acc -8)
(cons 'acc +45)
(cons 'jmp +49)
(cons 'acc +8)
(cons 'acc +22)
(cons 'jmp +209)
(cons 'acc +44)
(cons 'jmp +66)
(cons 'acc +7)
(cons 'acc -7)
(cons 'acc +48)
(cons 'jmp +318)
(cons 'nop +398)
(cons 'acc +2)
(cons 'jmp +16)
(cons 'nop +207)
(cons 'nop +358)
(cons 'acc +45)
(cons 'acc +48)
(cons 'jmp +267)
(cons 'nop +248)
(cons 'acc +26)
(cons 'jmp +307)
(cons 'acc +27)
(cons 'jmp -197)
(cons 'jmp -68)
(cons 'acc +34)
(cons 'acc +25)
(cons 'acc -13)
(cons 'jmp +133)
(cons 'jmp -77)
(cons 'acc -13)
(cons 'acc +10)
(cons 'jmp -193)
(cons 'jmp -62)
(cons 'acc +4)
(cons 'acc -14)
(cons 'jmp +261)
(cons 'jmp +151)
(cons 'jmp +208)
(cons 'acc -10)
(cons 'jmp +40)
(cons 'acc +31)
(cons 'jmp -216)
(cons 'acc +23)
(cons 'acc +34)
(cons 'jmp +364)
(cons 'nop +205)
(cons 'acc -3)
(cons 'acc +14)
(cons 'jmp +59)
(cons 'nop +359)
(cons 'acc -4)
(cons 'jmp +1)
(cons 'jmp -248)
(cons 'acc +47)
(cons 'acc +35)
(cons 'jmp +184)
(cons 'acc +16)
(cons 'nop -92)
(cons 'acc -12)
(cons 'jmp +354)
(cons 'acc +27)
(cons 'jmp -152)
(cons 'acc -14)
(cons 'acc -16)
(cons 'acc +43)
(cons 'jmp +147)
(cons 'acc +45)
(cons 'acc +24)
(cons 'acc +6)
(cons 'nop -46)
(cons 'jmp +21)
(cons 'acc +26)
(cons 'jmp +1)
(cons 'jmp +293)
(cons 'acc -8)
(cons 'acc +12)
(cons 'acc -19)
(cons 'acc -9)
(cons 'jmp +94)
(cons 'jmp +299)
(cons 'acc +10)
(cons 'acc -2)
(cons 'jmp +75)
(cons 'acc -7)
(cons 'acc +3)
(cons 'acc +47)
(cons 'jmp +171)
(cons 'acc +16)
(cons 'acc +44)
(cons 'acc -3)
(cons 'jmp +14)
(cons 'acc +30)
(cons 'acc +34)
(cons 'jmp -178)
(cons 'acc +35)
(cons 'nop -238)
(cons 'acc +39)
(cons 'jmp +1)
(cons 'jmp -133)
(cons 'acc +34)
(cons 'acc -6)
(cons 'jmp -276)
(cons 'acc +1)
(cons 'jmp -207)
(cons 'acc +10)
(cons 'jmp -43)
(cons 'jmp -302)
(cons 'acc -1)
(cons 'nop -29)
(cons 'jmp +1)
(cons 'acc +17)
(cons 'jmp -281)
(cons 'acc +17)
(cons 'jmp -109)
(cons 'jmp +1)
(cons 'acc +13)
(cons 'nop -9)
(cons 'jmp +245)
(cons 'acc +5)
(cons 'nop -15)
(cons 'acc +3)
(cons 'acc +7)
(cons 'jmp +65)
(cons 'acc -11)
(cons 'jmp -313)
(cons 'acc +47)
(cons 'jmp +29)
(cons 'jmp -289)
(cons 'acc +18)
(cons 'acc -17)
(cons 'nop +73)
(cons 'acc -12)
(cons 'jmp +80)
(cons 'acc +32)
(cons 'acc -4)
(cons 'acc +3)
(cons 'jmp -126)
(cons 'acc +16)
(cons 'jmp -275)
(cons 'nop -188)
(cons 'acc -3)
(cons 'acc +14)
(cons 'jmp -155)
(cons 'acc +33)
(cons 'acc -19)
(cons 'nop -166)
(cons 'acc +20)
(cons 'jmp +30)
(cons 'nop -169)
(cons 'acc +49)
(cons 'nop +168)
(cons 'jmp -24)
(cons 'nop -345)
(cons 'acc +34)
(cons 'jmp -40)
(cons 'jmp -56)
(cons 'jmp +29)
(cons 'jmp +191)
(cons 'acc +24)
(cons 'jmp +219)
(cons 'acc +34)
(cons 'acc +27)
(cons 'acc +11)
(cons 'jmp -260)
(cons 'jmp -339)
(cons 'acc +15)
(cons 'nop +16)
(cons 'jmp +1)
(cons 'jmp +138)
(cons 'jmp +1)
(cons 'jmp +1)
(cons 'jmp +14)
(cons 'acc -11)
(cons 'acc +45)
(cons 'jmp -19)
(cons 'acc +0)
(cons 'jmp +27)
(cons 'acc +0)
(cons 'nop +128)
(cons 'jmp -65)
(cons 'nop -23)
(cons 'jmp -318)
(cons 'jmp -325)
(cons 'jmp +1)
(cons 'jmp -229)
(cons 'jmp -270)
(cons 'jmp -137)
(cons 'acc +34)
(cons 'acc +7)
(cons 'jmp +1)
(cons 'jmp -346)
(cons 'acc +18)
(cons 'jmp +37)
(cons 'acc +40)
(cons 'acc -16)
(cons 'nop -146)
(cons 'acc +35)
(cons 'jmp -12)
(cons 'acc +1)
(cons 'acc +27)
(cons 'acc +44)
(cons 'acc +8)
(cons 'jmp -276)
(cons 'acc +16)
(cons 'acc +42)
(cons 'nop -342)
(cons 'acc +13)
(cons 'jmp -165)
(cons 'acc -11)
(cons 'acc -17)
(cons 'acc -10)
(cons 'jmp -26)
(cons 'acc +10)
(cons 'acc +43)
(cons 'jmp -276)
(cons 'acc +5)
(cons 'acc +34)
(cons 'acc +17)
(cons 'acc -9)
(cons 'jmp +99)
(cons 'acc +29)
(cons 'jmp -370)
(cons 'acc -11)
(cons 'jmp -412)
(cons 'acc +47)
(cons 'acc +21)
(cons 'acc -12)
(cons 'jmp -136)
(cons 'jmp -124)
(cons 'acc +12)
(cons 'acc +0)
(cons 'acc +25)
(cons 'acc +27)
(cons 'jmp -290)
(cons 'acc +5)
(cons 'acc +49)
(cons 'acc +32)
(cons 'nop +29)
(cons 'jmp -202)
(cons 'nop -296)
(cons 'acc -12)
(cons 'acc +9)
(cons 'acc +21)
(cons 'jmp +23)
(cons 'jmp -345)
(cons 'acc +26)
(cons 'nop -123)
(cons 'jmp -373)
(cons 'nop +118)
(cons 'jmp +43)
(cons 'acc -15)
(cons 'jmp -386)
(cons 'jmp +1)
(cons 'nop -370)
(cons 'acc +47)
(cons 'nop -141)
(cons 'jmp -426)
(cons 'acc +42)
(cons 'acc +12)
(cons 'acc +4)
(cons 'nop -103)
(cons 'jmp -122)
(cons 'acc +23)
(cons 'acc -4)
(cons 'acc +11)
(cons 'jmp -314)
(cons 'jmp -73)
(cons 'nop -1)
(cons 'jmp -411)
(cons 'acc +13)
(cons 'acc +9)
(cons 'nop -372)
(cons 'jmp -293)
(cons 'acc +46)
(cons 'acc +3)
(cons 'acc -1)
(cons 'jmp +86)
(cons 'acc +36)
(cons 'jmp +100)
(cons 'acc +27)
(cons 'acc +49)
(cons 'nop -4)
(cons 'acc +47)
(cons 'jmp -445)
(cons 'acc +31)
(cons 'acc +47)
(cons 'acc -11)
(cons 'acc +14)
(cons 'jmp -181)
(cons 'nop -438)
(cons 'acc +31)
(cons 'jmp -428)
(cons 'nop -115)
(cons 'nop -244)
(cons 'jmp -464)
(cons 'jmp -29)
(cons 'nop -240)
(cons 'jmp -241)
(cons 'acc -12)
(cons 'jmp -329)
(cons 'nop +78)
(cons 'acc +6)
(cons 'jmp +1)
(cons 'acc +49)
(cons 'jmp -322)
(cons 'jmp -133)
(cons 'acc +20)
(cons 'nop -83)
(cons 'acc +35)
(cons 'acc +29)
(cons 'jmp -41)
(cons 'acc +15)
(cons 'jmp -46)
(cons 'jmp -29)
(cons 'acc +45)
(cons 'acc -14)
(cons 'acc +21)
(cons 'jmp -366)
(cons 'nop +84)
(cons 'acc -6)
(cons 'acc +25)
(cons 'acc -17)
(cons 'jmp -326)
(cons 'acc -5)
(cons 'nop -159)
(cons 'acc +5)
(cons 'jmp -171)
(cons 'acc +42)
(cons 'jmp -28)
(cons 'acc +42)
(cons 'acc -11)
(cons 'acc +45)
(cons 'acc +19)
(cons 'jmp -305)
(cons 'acc +38)
(cons 'acc -13)
(cons 'acc -16)
(cons 'jmp -134)
(cons 'acc +45)
(cons 'jmp -256)
(cons 'acc -15)
(cons 'acc -18)
(cons 'acc +28)
(cons 'jmp -114)
(cons 'acc -11)
(cons 'acc +47)
(cons 'nop -420)
(cons 'jmp -90)
(cons 'nop -330)
(cons 'jmp +13)
(cons 'acc -15)
(cons 'acc +9)
(cons 'jmp -159)
(cons 'acc -12)
(cons 'acc +0)
(cons 'acc +0)
(cons 'jmp -538)
(cons 'acc +31)
(cons 'acc +24)
(cons 'acc +32)
(cons 'acc -16)
(cons 'jmp -95)
(cons 'jmp -466)
(cons 'acc +19)
(cons 'acc +2)
(cons 'jmp -172)
(cons 'acc -12)
(cons 'jmp -207)
(cons 'acc +39)
(cons 'acc +18)
(cons 'acc +5)
(cons 'jmp -211)
(cons 'nop -507)
(cons 'jmp +1)
(cons 'jmp -197)
(cons 'nop -227)
(cons 'acc +28)
(cons 'jmp -494)
(cons 'acc +22)
(cons 'acc +2)
(cons 'acc -14)
(cons 'jmp -377)
(cons 'acc +8)
(cons 'acc +29)
(cons 'jmp -573)
(cons 'acc -17)
(cons 'acc +14)
(cons 'acc +29)
(cons 'acc +11)
(cons 'jmp -351)
(cons 'acc +9)
(cons 'nop -540)
(cons 'acc +30)
(cons 'nop -344)
(cons 'jmp -564)
(cons 'acc -4)
(cons 'nop -465)
(cons 'jmp -293)
(cons 'acc -18)
(cons 'acc +5)
(cons 'acc +29)
(cons 'jmp -302)
(cons 'acc -17)
(cons 'acc +14)
(cons 'acc +2)
(cons 'acc -11)
(cons 'jmp -527)
(cons 'jmp -563)
(cons 'acc +14)
(cons 'acc +10)
(cons 'jmp -505)
(cons 'acc +43)
(cons 'jmp -188)
(cons 'nop -448)
(cons 'acc +44)
(cons 'acc +3)
(cons 'acc +16)
(cons 'jmp +1)
))
)

(define visited '())
(define ind 0)
(define inst)
(define acc 0)

(do
  ()
  ((member ind visited))
  (set! visited (cons ind visited))
  (set! inst (list-ref input ind))
  (cond
    ((eq? (car inst) 'nop)
      (set! ind (1+ ind))
    )
    ((eq? (car inst) 'acc)
      (set! acc (+ acc (cdr inst)))
      (set! ind (1+ ind))
    )
    ((eq? (car inst) 'jmp)
      (set! ind (+ ind (cdr inst)))
    )
  )
)

(pp visited)
(pp acc)
