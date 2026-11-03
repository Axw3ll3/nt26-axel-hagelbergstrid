## A

Pingen mellan Filservern och PC-Boras funkar inte då routrarna saknar väg ner till näten, de vet bara vägen till varandra. 

Output från 'show ip route static':


<img width="330" height="125" alt="Screenshot From 2026-11-02 15-16-48" src="https://github.com/user-attachments/assets/78acae7d-37f1-4770-a2bd-f8efa15017e6" />



Output från 'PC-Boras':


<img width="888" height="477" alt="Screenshot From 2026-11-02 15-19-10" src="https://github.com/user-attachments/assets/665d4a78-cd2c-4077-9ef1-b79fb8978420" />


# VG
Trafiken går via Nordvik eftersom längsta prefix matchingen i denna fråga går mot 0.0.0.0 0.0.0.0 (gateway of last resort) då den inte har en annan matchande IP route. Den tar vägen via Nordvik eftersom den har lägre värde på sin administrativa distans (1) medan vi satte reservvägen på AD 5.

I detta scenario försvinner svaret in i ett svart håll då den saknar returväg. Då bara ena porten är nere kommer Borås skicka via direktlänken till Mölndal, men då Mölndals last resort fortfarande pekar mot Nordvik kommer den länken hamna i prio och reservvägen (vilket i detta fall också är returvägen) kommer saknas för Mölndal. Värt att notera att om båda länkarna mot Nordvik (både från Mölndal och Borås) ligger nere tar reservlänkarna över och de kommer kunna kontakta varandra då de tar över gateway of last resort och får sin returadress. 

I hub & spoke med 10 kontor kommer det krävas 18 statiska rutter eftersom alla spokes behöver en rutt till hubben och hubben behöver en rutt tillbaka. Så 9 spokes till 1 hubb blir 9 vägar och 1 hubb ut till 9 spokes blir 9 till. 9 + 9 = 18 vägar. Fördelen med detta är att de är lätt att hålla reda på och lätt att lägga till då det bara behövs 2 nya rutter för varje ny enhet. Nackdelen är att det kan vara bottleneck (högre belastning).

I mesh behöver man en länk till varje ställe, sedan är allt kopplat till varandra. 10 routrar som har 9 vägar (då den inte kräver vägen till sig själv) gånger 10 routrar blir 90. Så 10 * 9 med andra ord. Fördelen är att det är snabbare kommunikation då allt är direktkopplat till varandra. Nackdelen är att det är mycket att hålla koll på och svårt att lägga till då alla enheter behöver en ny rutt till den nya enheten. 

## B
Pingen fastnar då ISP inte har någon destination eller vet vart den ska skicka 192.168.1.10 pingen, så den slänger bara iväg paketet. Den har inte heller en rutt att returnera sitt svar att den tagit emot pingen, då den inte vet vart pingen ska eller hur den ska svara tillbaka slänger den bort paketet.

