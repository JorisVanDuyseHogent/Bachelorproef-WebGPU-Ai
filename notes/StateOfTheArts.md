# State of the arts

## Evaluation of Theperformance of Webgpu in Acluster of Web-Browsersfor Scientific Computing

> The development and widespread of Internet browsers and technologies make them a tool that can be used for many scientific problems. This raises the ques-tion of whether Internet browsers, together with WebGPU and WebRTC, can be used to do scalable computing in a distributed cluster. This thesis answers the question by implementing a peer-to-peer cluster and testing it with two prob- lems, Matrix multiplication and Mandelbrot sets generation. The experimental results show that computing embarrassingly parallel problems are scalable with more than 75% efficiency.

## Running LLMs in the Browser with Rust + WebGPU

Zoals Fleetwood opmerkt zijn er al meerdere implementaties van ML op de web maar deze worden beschikbaar gesteld door servers en er wordt dus nog geen gebruik gemaakt van client-sided WebGPU rendering. Fleetwood beweert dat het essentieel zal zijn dat modellen lokaal worden gedraaid om de echte *'real-time'* te ondersteunen.

Ook worden er bij techonlogië zoals *language chain*; hierbij worden meerdere AI-modellen gebruikt om de functionaliteit van webapplicatie uit te breiden. Deze geweldige functionaliteit komt helaas met een hele grote kost.

Zo merkt (Huyen2023) op in haar onderzoek dat de kost van het draaien van AI-modellen in een productie omgeving enorm hoog kan oplopen zodat winstgevendheid in gevaar loopt. Dit is wel enkel het geval wanneer modellen suboptimaal worden ingezet zoals Fleetwood ook opmerkt.

WGSL is helaas al opgemerkt als een moeilijke shader language om mee te werken (Madrigal2023). Volgens Fleetwood is dit echter niet het geval en hij vindt dat de syntax toegangkelijk is omdat het veel invloeden heeft van Rust. Een populaire opkomend taaltje.

Fleedwood beweert zelf competitie te kunnen bieden aan open AI met zijn implementatie van het FLAN-T5 model van Google. Dit uiteraard wel voor beperkte use cases maar het is toch al een goed begin.

WebGPU laat misschien wel toe dat er rekenkracht beschikbaar wordt gesteld aan de browser maar dit wil niet zeggen dat hierdoor het probleem van draaien van lokale complexe modellen is opgelost. Er is namelijk ook een geheugen limitatie, een model moet worden ingeladen en dit liefts in VRAM van de grafische kaart. Hier kan dus potentieel een *bottleneck* ontstaan. Het efficient inladen en beschikbaar stellen van deze modellen is dus essentieel. Dit stelt Fleedwood ook vast waar hij opmerkt ... 

## WebGPU — All of the cores, none of the canvas 

Computationele taken uitvoeren lokaal in de browser was tot voor kort een complexe en inefficiente taak. Om dit met WebGL 1 te doen moet deze data eerst als een *texture* worden geencodeerd daarna gedecodeerd in een shader. Op dat moment moeten de calculaties worden uitgevoerd, deze calculaties moeten opnieuw worden geencodeerd tot een texture alvorens met de resultaten kan worden verder gewerkt. (Surma) Deze lange onnodige complexiteit komt verder uit het feit dat WebGL werd ontworpen voor het weergeven van grafische elementen, en dus niet om computationele taken uit te voeren zoals *machine learning* of het minen van *crypto currency*. Volgens (Surma) verbeterde de situatie wel met WebGL 2, maar de support voor deze API was beperkt en hierdoor kwam de proleferatie van computatie in de browser niet tot stand.

Omdat WebGPU wordt gestandaardiseerd door het World Wide Web Consortium, krijgt het dus ook een grotere ondersteuning en hierdoor kan deze technologie wel tot een revolutie leiden in Web rendering en computatie. Want in tegenstelling tot de beperkte ondersteuning van WebGL 2 zitten bij WebGPU wel alle browsers mee in het ontwikkelings process. (Surma)

De werking van een GPU is heel complex, hier wordt dus vaak te snel over gegaan. Er wordt door meerdere applicaties simultaan data naar het beeldscherm geprojecteerd en hierbij wordt dus de grafische kaart opgedeeld, de veiligheids implicaties hiervan zijn niet te onderschatten omdat deze applicaties elkaar niet mogen kunnen beinvloeden of data van elkaar mogen uitlezen. Voor elke applicatie lijkt het dus dat deze monopolie heeft over de grafische kaart maar eigenlijk wordt de rekenkracht verdeeld. Dit leidt ertoe dat de status van uitgevoerde computaties moeten worden bijgehouden omdat er altijd parallel wordt gewerkt. Programmeren voor General Purpose GPU verloopt dus altijd op een multi threaded asynchrone manier waar dus rekening mee moet gehouden worden. (Surma)

##  From WebGL to WebGPU

**Global State**
Een groot probleem dat werd opgelost bij WebGPU is het verwijderen van de *global state* die beschikbaar was in WebGL, deze global state zorgde ervoor dat ontwikkelaars makkelijk fouten konden introduceren in hun code. WebGPU vervangt het global state gedrag van WebGL met pipelines die niet mutable zijn eenmaal ze zijn aangemaakt.
Deze global state zorgde erdus voor dat het maken van grote robuste applicaties moeilijk was en leide tot fragile code volgens Baufort.

-- not finished here


## A case for client-side machine learning

Fleetwood merkt op dat er een paradigm verandering aankomt in hoe ai-modellen worden getrained. De huidige techonologie werkt als volgt; een hoeveelheid informatie wordt door de gebruiker voorzien en opgestuurd naar een model dat draait in de cloud, dit model produceert een antwoord dat terug aan de gebruiker wordt voorgelegd. Deze paradigm is enigsinds satis in dat het model dat draait in de cloud niet veranderlijk is. Fleetwood geloofd er in dat een toekomsige standaard met modellen die dynamish opgebouwd worden de toekoms is. Dit wil zeggen dat gewichten die worden toegepast op een AI-model gepersonaliseerd zijn voor de gebruiker.

Het is belangrijk om hierbij de privacy aspecten te herkennen, ook valt op te merken dat computatie op het web en dus WebGPU; een kaalisator zou kunnen zijn voor zo een paradigm verandering.

> "It would be optimal if the subset of weights that get updated to learn about the user remained on their device." Fleetwood

Wat Fleetwood ook opmerkt is dat er bij het draaien van een AI-technologieen vaak meerdere modellan serieel aan te pas komen. Deze modellen werken dan voort op informatie die reeds werd gegenereerd door een ander model. Deze technologie zou dus toestaan een hybride cloud te maken waarbij een deel van de computationele vereisten worden overgedragen aan de eindgebruiker.

Er moet wel worden benadrukt dat het downloaden van modellen een groot struikelblok voor de technologie kan betekenen. Veel modellen worden niet publiek gemaakt dus die kunnen van deze implementatie geen gebruik maken. Modellen die te groot zijn en er dus voor zorgen dat de eindgebruiker initieel moet wachten tot deze gedownload zijn alvorens de webapplicatie volledig beschikbaar is leiden tot een gedegradeerde bruikbaarheid. Maar volgens Fleetwood zijn dit problemen die door middel van compressie en cashing grootendeels verholpen kunnen worden.

## WebGPU computations performance in comparison to WebGL

Uit de ondervindingen van Radin blijkt dat WebGPU 3.5 keer sneller is dan WebGL simpele matric multiplicaties. Dit komt enerzijds omdat het proces om de berekeningen uit te voeren met WebGPU een stuk simpeler omdat WebGPU compute shaders ondersteunt en WebGL dit niet doet. Om computatie uit te voeren met WebGL is het namelijk vereist dat de data eerst wordt omgezet naar pixels zodat deze met een pixel shader kunnen worden berekent. Het nadeel hiervan is dat er een afhankelijkheid is op de canvas, omdat het gaat over het renderen van pixels. Radin ondervond hier dat WebGL de matrix multiplicatie niet ondersteund boven de 4096 bij 4096, dit komt door de fysieke limitatie van het canvas object. Maar volgens mdn web docs staat deze op 10.000 bij 10.000 tenzij de browser dit zelf limiteerd.