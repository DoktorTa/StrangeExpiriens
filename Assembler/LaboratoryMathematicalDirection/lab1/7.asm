.486
.MODEL Flat, StdCall ; StdCall - мантра
include \masm32\include\msvcrt.inc
includelib \masm32\lib\msvcrt.lib

.data
Format 	db 	' %d', 0
res1	dd	?
res2	dd	?
res3	dd	?
.CODE
; Какой знак имеет остаток от деления положительного числа на отрицательное? 
; От деления отрицательного числа на положительное? 
; От деления отрицательного на отрицательное? 
; Продемонстрируйте ответ на соответствующей программе, в которой должно
; производиться три деления; модуль делимого и делителя в начале записаны в переменных a и b, 
; а остатки — в переменных res1, res2 и res3, соответственно. Ответы на вопросы запишите в комментарии.
main:
	xor		edx,	edx
	mov		eax,	10
	mov		ebx,	-5
	div		ebx
	mov		res1,	edx	; 0x0A 10
	invoke crt_printf, addr Format, edx

	xor		edx,	edx
	mov		eax,	-10
	mov		ebx,	5
	div		ebx
	mov		res2,	edx	; 0x01 1
	invoke crt_printf, addr Format, edx
	
	xor		edx,	edx
	mov		eax,	-10
	mov		ebx,	-5
	div		ebx
	mov		res3,	edx	; 0xf6 0xff 0xff 0xff - не ебу биг или литл эндианы -10
	invoke crt_printf, addr Format, edx

	ret
	
end main