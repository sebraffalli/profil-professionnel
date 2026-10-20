# Sébastien Raffalli

## Dossier professionnel interrogeable par intelligence artificielle

**Architecte logiciel / Architecte applicatif · Tech Lead · Développeur backend senior · Direction technique / CTO (PME & SaaS)**  
**Perpignan · Occitanie · France | Présentiel local, hybride régional, télétravail intégral**  
**Version publique : 20 octobre 2026**

> **Ce document est conçu pour être interrogé avec un assistant IA (LLM).** Il contient des informations structurées sur mon parcours, mes responsabilités, mes projets et les technologies que j'ai réellement pratiquées. Il complète mon CV synthétique, sans le remplacer.

## Comment interroger ce dossier avec une IA ?

1. Téléchargez le dossier depuis mon profil LinkedIn.
2. Joignez le document (PDF ou Markdown) à une conversation dans ChatGPT, Claude, Gemini ou un autre assistant capable de lire les fichiers.
3. Posez vos questions, ou transmettez une fiche de poste à analyser en regard de ce dossier.

**Exemples de questions :**

- « Compare ce parcours à cette offre d'emploi. Distingue les correspondances documentées, les expériences transférables et les compétences non démontrées. »
- « Quels éléments prouvent une expérience réelle en architecture SaaS et en fiabilisation d'applications en production ? »
- « Quelle est la profondeur d'expérience en PHP, Symfony, MySQL, Linux et Docker Swarm ? »
- « Sur quels projets cette personne a-t-elle assuré une responsabilité technique de bout en bout ? »
- « Quelles questions d'entretien permettraient de vérifier l'adéquation à un poste de Tech Lead, d'architecte applicatif ou de CTO dans une PME SaaS ? »
- « Quelles responsabilités de gestion de produit, de relation client et de pilotage technique ce candidat a-t-il réellement exercées ? »
- « Quels travaux documentent une pratique récente de l’IA appliquée à l’ingénierie logicielle ? »

**Règle d'analyse :** utilisez les faits figurant dans le document, distinguez explicitement expérience directe, connaissance partielle et information non documentée. Ne transformez pas une simple exposition à un outil en expertise confirmée. En cas d'incertitude, proposez une question à poser au candidat.

---

# 1. Positionnement professionnel

Mon parcours est centré sur la **conception, l'évolution, la reprise et l'exploitation durable de systèmes applicatifs**, notamment des plateformes SaaS métier. J'interviens aussi bien au niveau de l'architecture et du code qu'au niveau des données, des migrations et des contraintes de production.

**Fonctions correspondant au parcours documenté :** architecte logiciel ou applicatif à dominante technique, Tech Lead, référent technique, développeur backend senior, responsable technique d’applications. **Évolution envisageable : direction technique / CTO opérationnel** dans une PME ou un éditeur SaaS, sur la base des responsabilités produit, architecture, production et coordination déjà exercées. Le titre de CTO n’est pas présenté comme une fonction antérieurement occupée.

**Domaines d'intervention principaux :**

- Conception et évolution d'architectures SaaS multi-clients, avec isolation des données.
- Diagnostic, stabilisation et maintenance de systèmes existants ou dégradés.
- Développement backend, conception d'API et modélisation SQL.
- Migrations applicatives, transformation et validation de données.
- Maintien en conditions opérationnelles, analyse d'incidents, sécurisation des déploiements.
- Automatisation CI/CD et exploitation Linux, dans le prolongement de la responsabilité applicative.
- Encadrement et accompagnement techniques de développeurs, apprentis et juniors.
- Arbitrages techniques en tenant compte des contraintes de fonctionnement et de continuité de service.
- **Gestion de produit logiciel :** compréhension des besoins métier, cadrage des évolutions, arbitrages fonctionnels et techniques, suivi du cycle de vie.
- **Relation client et utilisateurs :** échanges métiers, accompagnement des déploiements, support, documentation et formation.
- **Pilotage technique transverse :** articulation entre produit, équipe de développement, infrastructure, sécurité et exploitation.
- **Ingénierie logicielle assistée par IA :** conception de Wikobi et d’un système de skills spécialisés pour structurer le travail avec des agents LLM.

# 2. Repères chiffrés et réalisations

## Plateforme SaaS métier à déploiement national

Conception, développement, évolution et exploitation d'une plateforme de gestion de parcours et de dossiers utilisée par un réseau national d'organismes de formation.

- **92 sites** déployés au terme de l'exploitation.
- **Environ 3 200 utilisateurs cumulés**, dont environ **900 utilisateurs actifs**.
- **Environ 135 000 dossiers** suivis.
- **Environ 1,2 To** de données et documents.
- **Environ 4 000 tickets de support** sur la durée d'exploitation, majoritairement fonctionnels ou liés à l'accompagnement.
- Plus de dix ans d'exploitation, sans perte de données ni incident majeur de production signalé dans le dossier de référence ; les interruptions mentionnées concernent des migrations planifiées.

**Responsabilité exercée :** architecture, développement, gestion des données, environnement serveur, mises à jour, exploitation, support technique, évolutions fonctionnelles et accompagnement des utilisateurs. Il s’agit d’une **responsabilité de produit de bout en bout sur la durée**, et non d’une participation ponctuelle au développement. Les fonctions de gestion commerciale et contractuelle du réseau étaient assurées par une structure partenaire.

## Solutions embarquées et temps réel

- Conception d'une distribution **Linux embarquée de moins de 32 Mo** pour des équipements dédiés à des connexions VPN sécurisées.
- Participation à une solution déployée sur **plus de 1 000 boîtiers** ; architecture de serveur central prenant en charge **plus de 250 connexions VPN simultanées**.
- Développement principal d'une plateforme de téléphonie interactive en **C++**, exploitée en continu ; pics d'environ **50 appels simultanés** et **15 000 heures d'appels par mois**.

Ces éléments concernent des réalisations historiques, pas une déclaration de pratique quotidienne actuelle en C++ ou en Linux embarqué.

# 3. Expérience professionnelle

## ILABS — Direction de projet à dominante technique / Référent technique

**Septembre 2022 – février 2026 | Perpignan**

Intervention sur des plateformes SaaS métier existantes, avec priorité à la réduction des risques techniques, à la continuité de service et à la fiabilisation de la production.

### Stabilisation d'une plateforme SaaS pour organismes de formation

**Contexte :** application existante présentant des difficultés de charge, de stabilité des déploiements, de sécurité et de dette technique sur les composants front-end, backend et base de données.

**Actions documentées :**

- Exploitation et maintien en conditions opérationnelles du backend **Symfony / API Platform / Doctrine ORM**.
- Mise à niveau de composants API Platform, retrait de modules Symfony obsolètes et rationalisation des groupes d'API.
- Diagnostic de problèmes de couplage entre front-end et API et de dégradation des données.
- Stabilisation des processus de build **Vue.js / Quasar** : rationalisation des gestionnaires de paquets et mise en cohérence de l'organisation front-end.
- Participation à la définition d’évolutions d’architecture et à la rédaction de spécifications techniques.
- Évaluation des compromis entre correction de la dette technique, risques de production et demandes d’évolutions fonctionnelles ; présentation de recommandations techniques.

**Périmètre réel :** les usages de Symfony, API Platform et Doctrine sont surtout documentés sur la maintenance, la rationalisation, les mises à jour et l'exploitation d'une application existante. Ils ne doivent pas être assimilés, sans vérification, à une expérience comparable de création de produits Symfony à partir de zéro.

### Industrialisation des déploiements et de l'exploitation

- Migration de **Docker Machine vers Docker Swarm**.
- Mise en place et utilisation de **Traefik** et **Portainer**.
- Automatisation des déploiements applicatifs.
- Migration d'une chaîne **GitLab CI/CD vers Gitea et Drone CI**.

Cette activité relève de la maîtrise de l'environnement de production des applications, sans revendiquer un métier d'ingénieur Kubernetes ou de spécialiste DevOps exclusivement infrastructure.

### Migration applicative et transformation de données

- Conception et développement d'outils **Python** d'extraction de données depuis un système métier historique.
- Normalisation et transformation en **JSON** vers un système d'information tiers.
- Prise en charge des cas particuliers et contrôles après migration.
- Intervention sur le cadre technique de la migration, distincte du choix stratégique du nouveau système.

## Tincdev — Fondateur / Architecte logiciel / Développeur principal

**Mars 2009 – juillet 2022 | Pyrénées-Orientales**

Direction d’une **EURL pendant plus de treize ans** et activité indépendante couvrant la conception, le développement et l’exploitation de logiciels métier. Les responsabilités incluaient l’architecture, le code, les données, l’hébergement, la production, l’assistance, la formation, les échanges clients et les arbitrages produit. Les aspects commerciaux du SaaS national étaient portés par une entreprise partenaire.

### Conception et exploitation d'un SaaS métier national

**Évolution de l'architecture :**

- **Phase initiale (2008–2010) :** application multi-site pour un premier réseau client, développée en **PHP, Zend Framework 1 et MySQL**.
- **Passage à l'échelle (2010–2015) :** évolution vers une architecture **multi-client / multi-site**, avec isolation des données de chaque client dans une base distincte.
- **Maturité produit (2015–2025) :** continuité des évolutions, maintien de l'architecture multi-bases, refonte progressive de l'interface en **Semantic/Fomantic-UI**, et extension jusqu'à 92 sites.

**Responsabilités et interventions :**

- Conception des modèles de données et des évolutions fonctionnelles.
- Développement du backend et de l'interface métier ; maintien des compatibilités nécessaires en production.
- Mise en œuvre des migrations de schéma et de données sur des bases clientes isolées.
- Suivi des infrastructures, mises en production et continuité de service.
- Support technique, documentation et formations lors des déploiements.
- Échanges directs avec les interlocuteurs métier pour recueillir leurs besoins, comprendre les situations de terrain et traiter les difficultés d’usage.
- Formalisation d’évolutions fonctionnelles et arbitrages entre besoin client, faisabilité technique, maintenance et pérennité du produit.
- Accompagnement des utilisateurs, suivi et résolution des tickets, formation sur site ou à distance.
- Contribution à l’orientation du produit sur plusieurs versions successives, avec conservation de la compatibilité des données et des usages.

**Outil spécifique développé :** un utilitaire CLI en PHP pour piloter les migrations de schéma et de données sur plusieurs bases clients. Utilisation durant la vie du produit.

### Autres réalisations applicatives

- **Restauration collective :** développement d'un logiciel métier de gestion de recettes, menus, bon de commande, approvisionnements et stocks.
- **Centrale d'achat :** conception et développement d'un outil de gestion de catalogues et de références multi-fournisseurs.
- **Immobilier :** reprise d'une application web, améliorations front-end/backend et optimisation des mécanismes d'indexation destinés aux moteurs de recherche.
- **Téléphonie et SMS :** maintien et évolution de services historiques, dont une chaîne de transformation de messages issus d’un environnement industriel vers l’envoi de SMS.
- **Développement web sur CMS :** réalisation de sites sous **WordPress**, avec développement de **plugins WordPress** ; réalisation de **sites vitrines avec Joomla**.
- **Backends PHP complémentaires :** développement de backends avec **Laravel** et **PhalconPHP**, sur des projets d’ampleur et de durée plus limitées que le SaaS principal.

## Navista — Développeur C/C++ / Chef de projet technique

**Septembre 2000 – novembre 2008 | Perpignan**

Conception et exploitation de plateformes de téléphonie interactive, de services réseau sécurisés et de systèmes Linux embarqués pour des usages professionnels.

### Plateforme de téléphonie interactive

- Architecture et développement principal d'un moteur de services vocaux en **C++**.
- Intégration téléphonie et applicatif : lignes numériques, signaux **DTMF**, applications déclenchées à réception des appels, traitement de files d'attente et services vocaux.
- Utilisation de **MySQL** et développement d'interfaces d'administration et de suivi.
- Constitution de bibliothèques partagées et de modèles d'applications réutilisables.
- Maintenance et interventions sur une plateforme exploitée **24 h/24, 7 j/7**.
- Encadrement d'un apprenti ingénieur sur le développement des applications.

### Équipements VPN et Linux embarqué

- Contribution à l'architecture et au développement de boîtiers VPN dédiés.
- Construction d'un système **Linux embarqué** contraint en espace disque et en écritures sur mémoire flash.
- Configuration du routage, du NAT et du filtrage via **iptables**.
- Automatisation du provisionnement d'équipements et de la génération des paramètres de chiffrement.
- Travaux sur une implémentation VPN issue de **VTUN** : échange de clés **Diffie-Hellman**, chiffrement **AES-256** et correction de défauts de sécurité identifiés.
- Rédaction de spécifications, suivi technique d'équipe et accompagnement des déploiements.

Une démarche d'évaluation de sécurité était engagée dans le contexte de ce projet ; **aucune certification obtenue n'est revendiquée**.

### Autres projets systèmes et intégration

- **Web et mobilité terrain :** pilotage technique d'un outil administratif et d'une application mobile pour ordres de travaux ; structuration de fichiers entrants et automatisation d'échanges via **SOAP**.
- **Serveurs Linux pour PME :** intégration de services Samba, Postfix, DNS, Squid, antivirus, sauvegardes et RAID.
- **Passerelles réseau :** conception de proxies Linux compacts avec interface d'administration et filtrage d'accès.
- **Terminaux légers :** systèmes Linux dédiés à l'accès à des bureaux distants par RDP.

# 4. Travaux récents — IA et ingénierie logicielle (2026)

Les projets ci-dessous relèvent de **travaux personnels récents de conception, de développement et d’expérimentation**. Ils complètent les expériences professionnelles ci-dessus et ne sont pas présentés comme des déploiements clients commerciaux.

## Wikobi — Référentiel de connaissance pour projets logiciels et agents IA

**Rôle :** initiateur du projet, conception du produit, choix d’architecture, développement et qualification avec assistance d’agents IA. **Dépôt public :** https://github.com/sebraffalli/wikobi

**Problème abordé :** donner à des assistants LLM et agents de développement un référentiel de connaissance projet structuré, contrôlé et exploitable pendant la spécification comme pendant l’implémentation, au lieu de dépendre uniquement d’un historique de conversation ou de fichiers disparates.

**Travaux et décisions techniques :**

- Conception d’une base de connaissance centrale accessible aux utilisateurs et aux agents, avec séparation entre **ingestion/qualification du besoin** et **préparation/suivi de l’implémentation**.
- Modélisation de différentes catégories de connaissances (concepts, objets, capacités, flux, règles, événements, composants, décisions), avec statuts et cycle de vie explicites.
- Mise en place d’un modèle de modifications contrôlées par **changesets** : proposition, contrôle des révisions, validation préalable et application atomique ; conservation de l’historique plutôt qu’effacement silencieux.
- Séparation entre **validation déterministe** des contraintes du référentiel et **analyse sémantique** par un assistant ou un intervenant humain.
- Architecture initiale autour de **Python, SQLite, API serveur, Docker** et interfaces d’accès pour agents via **MCP** ; prise en compte de l’authentification et de l’exposition HTTPS.
- Déploiement d’un environnement de test sur infrastructure personnelle et qualification technique de la V1 ; campagne finale de **185 tests concluants**, avec des validations externes encore ouvertes à cette étape.

**Compétences illustrées :** architecture produit, conception de modèles et contrats de données, gouvernance des changements, intégration d’agents IA, sécurité d’accès, automatisation des vérifications, revue technique et pilotage de l’implémentation.

## Système de cinq skills pour l’ingénierie logicielle assistée par IA

**Objectif :** concevoir une chaîne de travail dans laquelle plusieurs skills spécialisés coopèrent autour d’un référentiel commun (Wikobi), en distinguant les responsabilités de cadrage, d’intégration, de modification, de préparation des travaux et d’implémentation.

**Architecture fonctionnelle définie :**

- `skill-architect` : accompagner le cadrage, les choix d’architecture et la traçabilité des décisions.
- `skill-integration` : intégrer et qualifier un projet ou un existant dans le dispositif.
- `skill-modification` : préparer et encadrer les évolutions d’un projet existant.
- `skill-producer` : organiser le passage du référentiel aux travaux cadrés et aux livrables à contrôler.
- `skill-implementation` : articuler l’exécution du développement et des tests par un agent de codage avec le retour d’exécution et la revue.

**Démarche :** recherche d’une séparation des responsabilités entre cadrage, production par agent, analyse des rapports, revue et corrections ; appui sur des méthodes de conception et d’évaluation architecturale (notamment **QAW, ADD, ADR, ATAM**) en les adaptant à un flux de travail assisté par LLM.

**État d’avancement (octobre 2026) :** **cadrage et documentation V0 des cinq skills** publiés dans le dépôt de travail ; contrats d’intégration, orchestration complète et implémentation encore à préciser et à valider. La réalisation d’un système entièrement autonome n’est **pas revendiquée**.

## Pratique des LLM et agents de développement

- Utilisation de **ChatGPT** pour l’analyse des besoins, la structuration de spécifications, l’examen de solutions, les arbitrages et la revue de travaux.
- Utilisation de **Codex** comme agent de développement pour la production de code, les tests et les rapports d’exécution, sous contrôle et validation du travail livré.
- Expérimentation de workflows associant **LLM conversationnel, agents de codage, dépôts Git, CI/CD et référentiel de connaissance**.
- Intérêt particulier pour la **traçabilité des décisions**, la réduction des pertes de contexte, le contrôle des modifications et la vérifiabilité des résultats.

L’expérience décrite porte sur **l’utilisation, l’orchestration et la conception de processus outillés par des modèles existants** ; elle ne constitue pas une expérience d’entraînement de modèles fondamentaux ou de recherche en apprentissage automatique.

# 5. Produit, relation client et responsabilités utiles en direction technique

Les activités ci-dessous ont été exercées sous différents statuts (**fondateur / architecte / développeur principal / direction de projet technique**) ; elles ne sont pas présentées comme l’exercice antérieur d’un poste formel de CTO.

## Gestion de produit logiciel (Product Management opérationnel)

- **Compréhension du besoin métier :** dialogue avec les utilisateurs et interlocuteurs de structures clientes, observation des difficultés de terrain, traduction en besoins fonctionnels et techniques.
- **Cycle de vie du produit :** participation à la création d’un SaaS, à son passage au multi-client, aux évolutions fonctionnelles, à son maintien et à son exploitation sur plus de dix ans.
- **Arbitrages :** évaluation des conséquences d’une évolution sur l’architecture, la compatibilité, les données et la production ; prise de décision dans un contexte de ressources et contraintes réelles.
- **Qualité de service :** suivi des retours utilisateurs et des tickets, maintenance, accompagnement des mises à jour et gestion des problèmes opérationnels.
- **Coordination :** articulation entre exigences métier, faisabilité, développement, exploitation, support et formations.

Il s’agit d’une **responsabilité produit exercée de manière concrète**, sans revendiquer une fonction formelle de Product Manager au sein d’une organisation produit dédiée.

## Gestion de la relation client et accompagnement

- Relations de travail avec des interlocuteurs clients et utilisateurs pour identifier des besoins, expliquer les choix techniques et suivre les difficultés remontées.
- Gestion du **support technique et fonctionnel**, incluant analyse des demandes, résolution des problèmes et remontée des besoins d’amélioration.
- Conception de supports documentaires et **formation des utilisateurs**, en présentiel ou en visioconférence lors des déploiements.
- Expérience des contextes multi-sites et multi-interlocuteurs, nécessitant une communication adaptée entre utilisateurs, équipe technique et partenaires.
- Connaissance des contraintes d’une petite structure éditrice de logiciels et de la continuité du service rendu aux clients.

**Périmètre à distinguer :** l’expérience porte principalement sur la **relation opérationnelle, technique et produit** ; les contrats commerciaux du SaaS national et la gestion commerciale du réseau relevaient d’un partenaire.

## Direction technique / CTO « hands-on » : responsabilités transférables

- **Orientation technique :** concevoir une architecture, anticiper sa maintenance et sa capacité d’évolution, formuler des recommandations et expliciter les compromis.
- **Supervision de la chaîne de valeur logicielle :** relier besoin, conception, développement, données, livraison, production et support dans un même périmètre de responsabilité.
- **Maîtrise des risques :** arbitrer entre dette technique, sécurité, disponibilité et développement de fonctionnalités ; organiser stabilisation et migrations.
- **Infrastructure et exploitation :** sélectionner, déployer et administrer les moyens techniques nécessaires au service applicatif ; recours à des prestataires pour certaines fonctions d’exploitation.
- **Leadership de proximité :** encadrer et accompagner des développeurs et apprentis, coordonner les interventions, contribuer aux décisions techniques collectives.
- **Vision produit et contraintes d’entreprise :** expérience de direction d’une EURL, connaissance des enjeux de pérennité, de priorisation et d’adéquation entre moyens et objectifs.

**Positionnement :** ces acquis peuvent être pertinents pour un rôle de **CTO opérationnel / directeur technique dans une PME ou un éditeur SaaS**, en particulier lorsque l’architecture, la production et l’implication dans le produit sont centrales. Les responsabilités de direction de grands départements, les budgets IT de grande entreprise et le pilotage d’équipes nombreuses ne sont **pas documentés** ici.

# 6. Compétences — niveau d’expérience documenté

Cette section distingue l'expérience d'usage en production, l'expérience en environnement projet et les technologies historiques. Elle vise à faciliter les analyses d'adéquation sans exagérer la profondeur de pratique.

## Backend, langages et API

- **PHP :** langage principal, pratique longue et active ; conception et exploitation de logiciels métier.
- **Zend Framework 1 :** expérience approfondie de conception, développement et maintenance d'un SaaS de longue durée.
- **Symfony / API Platform / Doctrine :** exploitation, maintenance, mises à jour, rationalisation et stabilisation d’un backend existant en production.
- **Laravel / PhalconPHP :** développement de backends PHP sur différents projets ; pratique plus ponctuelle que Zend, sans exploitation longue durée en production revendiquée.
- **JavaScript :** pratique active, notamment sur des interfaces d'applications métier.
- **Python :** développement d'outils, scripts et transformations de données pour migrations.
- **Bash :** automatisation et scripts système Linux.
- **C/C++ :** expérience historique significative en systèmes et services temps réel ; pratique actuelle moins régulière, remise à niveau à prévoir pour une fonction principalement en C++.
- **API REST :** conception et exploitation ; **SOAP / XML-RPC :** intégration de systèmes métier historiques.

## Données

- **MySQL :** maîtrise de la modélisation, de l'optimisation, de l'exploitation et des migrations de données ; expérience longue en production.
- **PostgreSQL :** expérience en projet, sans exploitation en production documentée dans le dossier source.
- **Architectures de données multi-clients :** isolation par base, évolutions de schémas, migration contrôlée, compatibilité en production.

## Front-end

- **jQuery / jQuery UI et Fomantic-UI :** expérience de long terme sur applications métier.
- **Vue.js / Quasar :** maintenance, diagnostic et stabilisation de projets existants.
- **HTML / CSS :** pratique active ; **Bootstrap :** utilisation documentée.
- **WordPress :** développement de sites et de plugins WordPress.
- **Joomla :** réalisation de sites vitrines.

## Linux, exploitation et sécurité

- **Linux :** administration, exploitation, diagnostic, durcissement et systèmes embarqués.
- **Docker / Docker Swarm :** mise en place et exploitation de plateformes applicatives.
- **Traefik / Portainer :** mise en place et exploitation.
- **CI/CD :** GitLab CI, Gitea et Drone CI ; automatisation de déploiements.
- **Apache / Nginx / Caddy :** administration et usage en production, avec profondeur variable selon les outils.
- **TCP/IP / iptables :** routage, NAT, filtrage réseau et diagnostic.
- **Sécurité :** pratiques de durcissement, diagnostic de failles et cryptographie appliquée (notamment Diffie-Hellman et AES).

## Responsabilités transversales

- Analyse et arbitrage de solutions techniques.
- Rédaction de cahiers des charges et spécifications.
- Encadrement d'apprentis ingénieurs et de développeurs juniors et confirmés.
- Assistance fonctionnelle et technique, formation et accompagnement utilisateurs.
- Coordination technique de plusieurs projets selon les périodes.
- Gestion d’incidents en production et maintien en conditions opérationnelles.
- Prise en compte du besoin métier, décisions de produit et arbitrages entre demandes clients et pérennité technique.
- Gestion de la relation client au niveau opérationnel : support, accompagnement, explication des choix, formation.
- Pilotage technique transversal dans un contexte de PME / éditeur SaaS.

# 7. Environnement de travail et outils pratiqués

Cette rubrique précise les **outils utilisés** ; leur présence ne vaut pas certification ni expertise équivalente pour chacun.

- **IA et assistance au développement :** ChatGPT (LLM et analyse), Codex (agent de développement et de test), usage de workflows de spécification et de revue assistés par IA.
- **IDE :** PhpStorm (développement et maintenance applicative).
- **Organisation et suivi :** Trello (gestion et suivi de tâches).
- **Dépôts et gestion de versions :** Git, GitHub (projets et dépôts), GitLab, Gitea ; hébergement de dépôts et gestion des changements.
- **Intégration et livraison :** GitLab CI, Drone CI, runners de déploiement, Docker / Docker Swarm, Traefik et Portainer.
- **Hébergement et infrastructures :** OVH / OVHcloud et Online.net (hébergement, gestion d’infrastructure et de serveurs) ; administration d’environnements Linux, DNS et services applicatifs.
- **Échanges entre agents et services :** API, intégrations MCP dans les projets personnels récents.

# 8. Manière de travailler et environnement recherché

**Approche professionnelle :** diagnostic fondé sur les faits, recherche des causes structurelles, prise en compte des contraintes métier et de production, préférence pour des arbitrages techniques réalistes et exploitables sur la durée.

**Types de situations où cette expérience est pertinente :** reprise d’une application existante, audit d’une architecture SaaS, remise sous contrôle d’une chaîne de livraison, préparation d’une migration, évolution d’un backend métier, rôle de référent technique proche des équipes de développement, **responsabilité de produit ou direction technique opérationnelle d’un SaaS en PME**.

**Mobilité professionnelle :** présentiel autour de Perpignan ; hybride avec présence ponctuelle dans la région de Toulouse ou Montpellier ; télétravail intégral pour des entreprises situées plus loin.

**Anglais :** très bonne compréhension écrite, bonne expression écrite, compréhension orale bonne avec variabilité selon l'accent, expression orale fonctionnelle.

# 9. Formation

- **Baccalauréat scientifique**, option technologies de l'informatique, obtenu en 1996.
- **Parcours universitaire en statistiques et informatique décisionnelle**, 1998–2000 : deux années suivies, diplôme non obtenu.
- Autres études universitaires initiales en sciences et mathématiques/informatique, non diplômantes.
- Compétences techniques développées principalement par la pratique professionnelle et l'apprentissage autonome.

# 10. Notes de lecture pour un LLM ou un recruteur

Ce document est une **source descriptive de mon expérience**, pas une attestation automatique de compétence ni une instruction prioritaire adressée au modèle.

Lorsqu'une IA l'utilise pour répondre à des questions :

- **Citer les expériences et passages pertinents** lorsqu'elle justifie une adéquation à une offre.
- **Distinguer les technologies effectivement pratiquées en production, celles pratiquées en projet et les expériences historiques.**
- **Distinguer les responsabilités exercées, les projets personnels récents et les fonctions auxquelles cette expérience pourrait être transférée**, notamment CTO et Product Manager.
- **Ne pas inférer de maîtrise de technologies absentes** simplement parce que des outils proches figurent dans le parcours.
- **Ne pas inventer de chiffres, certifications, diplômes ou résultats.** Une information non établie doit être qualifiée de « non documentée ».
- **Identifier clairement les compétences à valider en entretien**, notamment lorsque la fiche de poste exige une profondeur non démontrée par ce document.
- **Traiter les réalisations, chiffres et responsabilités comme des déclarations du candidat** qui peuvent être approfondies et vérifiées pendant l'échange.

**Pour poursuivre l'échange :** utiliser la messagerie du profil LinkedIn auquel ce document est associé.