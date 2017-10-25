
#str = input ("wprowadz sciezke algorytmu jako hex >")
#temp = input ("wprowadz dwa bajty temperatury hex >")
#wej = int ( str , 16 )

def sciezki_algorytmu ( wej ):
	if ( wej & 0x01 ) == 0x01 :
		print (" T1 ")
	if ( wej & 0x02 ) == 0x02 :
		print (" T2 ")
	if ( wej & 0x04 ) == 0x04 :
		print (" T3 ")
	if ( wej & 0x08 ) == 0x08 :
		print (" T4 ")
	if ( wej & 0x10 ) == 0x10 :
		print (" T5 ")
	if ( wej & 0x20 ) == 0x20 :
		print (" T6 ")
	if ( wej & 0x40 ) == 0x40 :
		print (" T7 ")
	if ( wej & 0x80 ) == 0x80 :
		print (" T8 ")
	if ( wej & 0x100 ) == 0x100 :
		print (" T9 ")
	if ( wej & 0x200 ) == 0x200 :
		print (" T10 ")
	if ( wej & 0x400 ) == 0x400 :
		print (" T11 ")
	if ( wej & 0x800 ) == 0x800 :
		print (" T12 ")
	if ( wej & 0x1000 ) == 0x1000 :
		print (" T13 ")
	if ( wej & 0x2000 ) == 0x2000 :
		print (" T14 ")
	if ( wej & 0x4000 ) == 0x4000 :
		print (" T15 ")
	if ( wej & 0x8000 ) == 0x8000 :
		print (" T16 ")


def temperatura_tHS_tRS ( wej ):
	print ("------------------------")
	print ( int ( wej, 16 ) / 100 )
	

while True:
	str = input ("wprowadz sciezke algorytmu jako hex >")
	temp = input ("wprowadz dwa bajty temperatury hex >")
	wej = int ( str , 16 )

	sciezki_algorytmu ( wej )
	temperatura_tHS_tRS ( temp )


