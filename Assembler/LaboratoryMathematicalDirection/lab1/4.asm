.486
.MODEL Flat, StdCall ; StdCall - мантра
include \masm32\include\msvcrt.inc
includelib \masm32\lib\msvcrt.lib

.data
Format db '%d', 0
; Это значит A - с типом dd (4 байта) = 10
A dd 10
B dd 20
D dd 30
E dd ?
.CODE
;4. Вычислите значение выражения a · b + d и занесите его в переменную e, где a, b, d, e —
;32-битные знаковые переменные. Считаем, что произведение a·b помещается в 32 бита.
main:
	; eax = 1, тоесть число a = 10
	; ebx = 2, тоесть число b = 20
	mov eax, A
	mov ebx, B
	
	; eax = eax * ebx (a * b)
	mul ebx
	
	mov ebx, D
	
	; eax = eax + ebx  (+ d)
	add eax, ebx
	
	; E = eax
	mov E, eax
	mov edx, E
		
	; Вывод результата на экран
	invoke crt_printf, addr Format, edx
	
	; И это мантра (пока что)
	ret
end main