package main

import (
	"context"
	"google.golang.org/grpc"
	"math/rand"
	"net"
	"github.com/wernerdweight/grpc-test/ovm"
)

type Server struct {
	ovm.UnimplementedOtazkyVaclavaMoravceServer
}

func (server *Server) VaclavMoravec (ctx context.Context, request *ovm.MoravecRequest) (*ovm.Response, error) {
	return getResponse(Moravec, request.Mood, nil, nil), nil
}

func (server *Server) VaclavKlaus (ctx context.Context, request *ovm.KlausRequest) (*ovm.Response, error) {
	return getResponse(Klaus, request.Mood, &request.Sport, nil), nil
}

func (server *Server) MilosZeman (ctx context.Context, request *ovm.ZemanRequest) (*ovm.Response, error) {
	return getResponse(Zeman, request.Mood, nil, &request.Booze), nil
}

func main() {
	lis, _ := net.Listen("tcp", ":50051")
	server := grpc.NewServer()
	ovm.RegisterOtazkyVaclavaMoravceServer(server, &Server{})
	server.Serve(lis)
}

// server implementation below

type Bloke string

const (
	Moravec Bloke = "Václav Moravec"
	Klaus Bloke = "Václav Klaus"
	Zeman Bloke = "Miloš Zeman"
)

var data = map[Bloke][]string{
	Moravec: {
		"A o čem se po dnešních otázkách začne mluvit?",
		"Promiňte, ale Vám to připadá normální?",
		"Není čas konečně zvýšit daň z nemovitosti?",
		"Pánové, nehádejte se prosím!",
		"Opravdu?",
		"Vy pánové vůbec neodpovídáte na moje dotazy.",
		"Kdo za to tedy může?",
		"Proč k tomu došlo?",
		"Je to v současné situaci moudré?",
		"Jak se toto dotkne střední třídy?",
		"Ale co samoživitelky?",
		"Je vám dobře?",
		"Nepřijde vám to ani trochu nevhodné?",
		"Tristan Tzara by tuto debatu nejspíš obdivoval, ale co na to divák?",
		"Tento způsob využití koncesionářských poplatků, zdá se mi poněkud nešťastný.",
		"Vy mi utíkáte od tématu.",
		"Pamatujete si, jak změna otázka?",
		"Na to jsem se ale neptal, můžete odpovědět?",
		"Kolik to celé bude ale stát?",
		"Není to v rozporu s programovým prohlášením vlády?",
	},
	Klaus: {
		"Ne. Ne. Takhle ale otázka přeci vůbec nestojí.",
		"Promiňte, a Vy jste kdo?",
		"To je velmi, ale velmi krátkozraké.",
		"Vy si ale nemyslíte, že na toto budu reagovat, že ne?",
		"Vlemi impertinentní. Styďte se!",
		"Vy jste lidská hyena.",
		"Nemám rád katastrofické scénáře.",
		"Tuto otázku kategoricky odmítám. Hlavně proto, že takovou otázku vůbec nepotřebujeme.",
		"O tom neumím hluboce filozofovat a filozofování o tomto ani moc nevěřím.",
		"Nejprve jsem váhal, jestli sem mám chodit, protože jsem si dovedl živě představit, jaké zploštělé, trivializované, povrchní, ofrněné, nafoukané, arogantní postoje tu budou od údajných odborníků zaznívat. Nicméně manželka mi docela správně říkala, prosím tě, jdi tam, protože je potřeba, aby to tam také někdo vysvětloval jiným způsobem.",
		"To není žádná věda. S vědou to nemá nic společného. Je to ideologie.",
		"Environmentalismus není nic jiného než novodobá inkarnace tradičního levičáctví.",
		"Žádné ničení planety nevidím, nikdy v životě jsem neviděl a nemyslím, že nějaký vážný a rozumný člověk by to mohl říci.",
		"Jedu lyžovat a stoupnu si do fronty u vleku, co bych dělal také jiného.",
		"Já vím, kde ty peníze jsou, ale proč to chcete vědět vy?",
		"Nečtu-li si doma celá desetiletí v encyklopediích, nebudu asi příliš často využívat ani Internet.",
		"Chápu, že Windows 10 je lepší než ťukání na psacím stroji v roce 1950 a produktivitu to nepochybně zvyšuje. Ale že by to zvýšilo o milimetr produktivitu české ekonomiky oproti Windows s číslem 9? Zvýšení nula, efekt nulový.",
		"Jak je to krásné být milován pitomci!",
		"Džíny jsem měl a mám, ale nikdy jsem neměl džínovou bundu. To pro mě bylo nesmírně cizí a falešné.",
		"Jsem přesvědčen, že jsem toho nevykonal málo a že to bude ve střízlivější chvíli, než je tato, doceněno.",
		"Novináři jsou největšími nepřáteli lidstva.",
		"Člověk přebíhá ulici na červenou a samozřejmě musí počítat s tím, že sklouzne a přejede ho auto.",
		"Myslím, že přečtu víc než kdokoliv jiný.",
		"Čokoládový krém je pravicový, salát levicová úchylka a antijídlo.",
		"Já v žádném případě netvrdím, že jsem bůh.",
		"Dali jsme si vepřový řízek, kuřecí řízek je levicové jídlo.",
		"To je děsivě, děsivě špatná teze.",
		"Angela Merkelová? Tak, že je to žena, to vím. Ale zapůsobit na ni nějakým mužským šarmem možné není.",
		"Prázdný a falešný Topol.",
		"Byla to nevýhra.",
		"Musím říct, že to nebylo pero, je to normální propiska. Aby nebyly nějaké velké oči.",
		"Mažu si vás z mobilu.",
	},
	Zeman: {
		"Pane redaktore, nemáte popelníček?",
		"Dovolte mi reagovat bonmotem.",
		"Víte co to je pasy, pane moderátore?",
		"Kunda sem, kunda tam.",
		"Kunda, pane redaktore, kunda je to.",
		"Bylo to vlevo dole.",
		"Jiří, je čas, kde jste?",
		"Šíří se fámy, že mám velmi rád becherovku a pivo. Obě jsou pravdivé.",
		"Novináři jsou pitomci, hnůj a fekálie.",
		"Já jsem si měl tu kulovnici přinést, když ne k projednávání státního rozpočtu, tak k těmto interpelacím.",
		"Navštivte půvabnou pražskou čtvrť, která se jmenuje Bohnice, a nechte se tam sakra do konce tohoto pořadu hospitalizovat.",
		"Smrt abstinentům a vegetariánům.",
		"Za celý svůj život jsem se nesetkal s blbějším a závistivějším stvořením.",
		"Můj vztah k zelenině je veskrze pozitivní. Žádám ovšem, aby mezi mne a ji byl vsunut transformační mezičlánek, který se jmenuje prase.",
		"Jak jistě dobře víte, na levici je více manipulovatelných idiotů.",
		"Peroutka je gentleman.",
		"Když jsem si chtěl zapálit v Bílém domě, George Bush jr. se díval dost divně.",
		"Jen pitomci říkají, že jsem nemocný.",
		"Jsem arogantní a jsem na to hrdý.",
		"Nejsem diktátor, bohužel.",
		"Novinářů je příliš mnoho, měli by se zlikvidovat.",
		"Rusko mě neplatí vodkou ani penězi.",
		"Sním o tom, že Rusko jednou vstoupí do EU.",
		"Vyžeňte toho kameramana, nebo ho zabiju.",
		"Vzhledem k tomu, že podporuji čínské investice a CEFC koupila Slavii, musím fandit Slavii.",
		"Zavřete pusu, pane redaktore. Když ji máte otevřenou, nesluší vám to.",
	},
}

func getResponse(bloke Bloke, mood ovm.Mood, sport *ovm.Sport, booze *ovm.Booze) *ovm.Response {
	var score int32 = 1
	if (sport != nil && *sport == ovm.Sport_EGO) || (booze != nil && *booze == ovm.Booze_VIROZA) {
		score += 5
	}
	if mood == ovm.Mood_GOOD {
		score += 3
	}
	if mood == ovm.Mood_NOT_THIS_SHIT_AGAIN {
		score -= 2
	}
	return &ovm.Response{
		Sentences: []*ovm.Sentence{
			{ Text: data[bloke][rand.Intn(len(data[bloke]))] },
		},
		Score: score,
	}
}