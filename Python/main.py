from random import randint
x=input('inserire')
y=['foro','foro conico','filettatura','foro lamato','raccordo','conicità','smusso','zgrinatura','asola','spallamento','nervataura','gola','chiavetta','albero scanalato','foro scanalato','sede per chiavetta','tornitura','aletta','stampaggio','fresatura','saldatura','foratura','rivettatura','rettifica','ruota dentata','vite','prigioniero','dado','bullone','rosetta','ingranaggio','puleggia','distanziatore','spina','guarnizione','anello radiale','grano','copiglia','giunto sferico','perno spina','ghiera','cuscinetto','boccola','mozzo','albero','flangia','albero a gomiti','ruota','pistone','biella','conchiglia','supporto']

while x!='stop':
    n=randint(1,len(y))
    print(y[n])
    x=input('')

x=input('inserire')
y=['hole','tapered hole','thread','counterbore','fillet','conical surface','chamfer','knurl','slot','collar','rib','groove','key','splined shaft','splined hole','keyseat','turning','lug','casting','milling','welding','drilling','rivet','grinding','gear','screw','stud','nut','bolt','washer','trasmissione gearset','pulley','spacer','pin','oring','seeger','socket screw','cotter','uniball','pin','locking nut','bearing','bushing','hub','shaft','flange','crankshaft','wheel','piston','connecting-rod','shell','support']

while x!='stop':
    n=randint(1,len(y))
    print(y[n])
    x=input('')
