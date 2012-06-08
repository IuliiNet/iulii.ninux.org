### routing mesh con batman-adv 

![batmand-adv logo](../img/batman-adv.png "il logo di batman-adv") 

[http://www.open-mesh.org/wiki/batman-adv/](http://www.open-mesh.org/wiki/batman-adv/ "homepage di batman-adv")

Batman-adv è un protocollo di routing per reti mesh, ottimizzato per l’utilizzo su reti  wireless. Il tipico scenario in cui questo protocollo viene utilizzato è una rete wireless adhoc multi-hop.

E' un protocollo su layer2, cioè instaura comunicazione con gli altri nodi della rete senza utilizzare i comuni indirizzi ip (che sono sul layer3). Per gestire il protocollo si utilizza l’eseguibile batctl (che può fornire utili informazioni sullo stato della mesh), anche se openwrt mette a disposizione un comodo file di configurazione che infatti si utilizzerà.

Quello che sarà necessario indicare a batman-adv sono i device da utilizzare per la mesh, e se il nodo in questione deve funzionare da gateway per internet o da client. Fatto questo, batman-adv creerà una nuova interfaccia (nel caso bat0) sulla quale si potrà lavorare sul layer3.

Grazie a tutte le bat0 di ogni device viene quindi a crearsi una struttura di nodi simile ad "un grande switch". Quindi ad ogni bat0 (o al bridge al quale appartiene)sarà possibile assegnare i suoi ip. Quindi ogni device batman-adv riuscirà a vedere, attraverso i suoi vicini, tutti gli altri nodi della rete.

Un primo aspetto molto interessante di questo approccio alla rete (che tra l’altro forniscono anche altri protocolli di routing come oslr, ed è quindi una caratteristica intrinseca delle reti mesh) è la creazione di una struttura a maglia, nella quale ogni nodo riesce a comunicare direttamente (single-hop) con un alto numero di nodi vicini. Si capisce che in questo modo, la caduta di un singolo nodo non pregiudica il collegamento di altri nodi, che infatti saranno in grado di trovare la strada per le loro comunicazioni attraverso gli altri vicini attivi.

In maniera complementare, l'aggiunta di un altro nodo alla rete mesh sarà automaticamente riconosciuta da tutti i suoi vicini, e quindi da tutti i nodi della rete mesh, contribuendo in questo modo alla crescita della rete.

Un peculiarità molto interessante di batman-adv, grazie anche alla presenza dei server dhcp sui gateway, è la capacità dei nodi senza accesso ad internet di trovare il server dhcp "migliore".