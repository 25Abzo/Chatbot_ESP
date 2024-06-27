import csv

data = [
    
    ["questions", "reponses"],
    ["Quelle est l'une des plus prestigieuses écoles d'ingénieur et de management en Afrique francophone?", "L'École supérieure polytechnique (ESP) de l'Université Cheikh Anta Diop de Dakar."],
    ["Quand a été créée l'ESP de Dakar?", "En 1964."],
    ["Combien de diplômés l'ESP a-t-elle formés au moins?", "Plus de 30 000 diplômés."],
    ["Quels types de diplômes l'ESP offre-t-elle?", "Diplôme universitaire de technologie (DUT), diplôme supérieur de technologie (DST), licence, diplôme d’ingénieur technologue (DIT), master, diplôme d’ingénieur de conception (DIC) et doctorat."],
    ["Que présente la troisième édition du catalogue des formations de l'ESP?", "L'ensemble des parcours de formation délivrés dans les six départements de l'ESP, les missions de l'ESP, les différentes formations offertes et les modalités d'admission à ces formations."],
    ["Quelle preuve le document du catalogue de formations fournit-il?", "La preuve que l'offre pédagogique de l'ESP est hautement professionnelle et l'une des plus complètes au Sénégal et en Afrique francophone."],
    ["À quoi sont régulièrement soumises les formations de l'ESP?", "À l'évaluation de l'Autorité nationale d'assurance qualité de l'enseignement supérieur (ANAQ-Sup)."],
    ["Pourquoi les formations de l'ESP sont-elles soumises à l'évaluation de l'ANAQ-Sup?", "Afin de garantir leur qualité, leur pertinence et leur adéquation aux besoins des entreprises et des communautés."],
    ["Qui participe aux formations de l'ESP?", "Des enseignants de métier et des professionnels issus des différents secteurs du monde socio-économique."],
    ["Comment l'ESP place-t-elle l'étudiant ou l'apprenant au cœur de son dispositif d'enseignement/apprentissage?", "Grâce à l'existence de laboratoires, halls de technologie équipés et adaptés aux besoins des formations."],
    ["Comment l'ESP maintient-elle ses relations avec le milieu du travail?", "Grâce à sa renommée et par la prise en charge des besoins de carrière dans son curriculum de formation."],
    ["Que prouve le réseau des alumni de l'ESP?", "Que la majorité des diplômés de l'ESP travaillent dans de grandes entreprises, tant au niveau national qu'international."],
    ["Quel message le directeur adresse-t-il aux étudiants à la fin de son mot?", "Bonne année universitaire."],
    ["Quelles étaient les anciennes dénominations de l'École Supérieure Polytechnique (ESP)?", "ENSUT (École Nationale Supérieure Universitaire de Technologie), IUT (Institut Universitaire de Technologie), IP (Institut Polytechnique)."],
    ["Quelle est la vocation de l'ESP?", "Une vocation interafricaine de l'Université Cheikh Anta Diop de Dakar (UCAD)."],
    ["Quand a été créée l'ESP et par quelle loi?", "Le 24 novembre 1984 par la loi n°94-78."],
    ["Quelle est la personnalité de l'ESP?", "L'ESP est dotée d'une personnalité juridique et de l'autonomie financière."],
    ["Quand l'ESP a-t-elle fêté ses 50 années?", "En 2014."],
    ["Quel événement majeur s'est produit le 20 mai 1964 concernant l'ESP?", "La création de l'Institut Polytechnique (IP), un établissement technique supérieur dépendant de l'Université de Dakar."],
    ["Quels décrets présidentiels ont créé l'IUT et quand?", "Les décrets présidentiels n°67-1230 et 67-1231 ont créé l'IUT le 15 novembre 1967."],
    ["Que s'est-il passé le 30 avril 1973 pour l'IUT?", "La promulgation de la loi 73-17 et le décret 73-387 ont permis à l'IUT de devenir un établissement public doté de la personnalité juridique et de l'autonomie financière."],
    ["Quelle réforme a eu lieu en 1973-1974 concernant l'ENTPB?", "L'École Nationale des Travaux Publics et Bâtiments (ENTPB) a été intégrée au département de génie civil de l'IUT et d'autres réformes ont été mises en place."],
    ["Quelle est la nouvelle appellation de l'Institut après avoir dispensé des enseignements en commerce et administration des entreprises?", "L'École Nationale Supérieure Universitaire de Technologie (ENSUT)."],
    ["Quels diplômes complémentaires l'Institut délivre-t-il?", "Diplôme d'Ingénieur en Technologie (DIT) et Diplôme d'Études Supérieures de Commerce et d'Administration des Entreprises (DESCAE)."],
    ["Quand la loi 94-78 a-t-elle créé l'École Supérieure Polytechnique (ESP)?", "Le 20 novembre 1994."],
    ["Quels établissements composent l'ESP créée par la loi 94-78?", "L'École Polytechnique de Thiès (EPT) et l'École Nationale Supérieure d'Enseignement Technique Professionnel (ENSET)."],
    ["De quelle division l'ESP s'est-elle séparée au moment de sa création en 1994?", "De sa division tertiaire devenue Institut Supérieur de Gestion (ISG), rattachée à la Faculté des Sciences Économiques de Gestion (FASEG)."],
    ["Combien de centres compose l'ESP et où sont-ils situés?", "Deux centres : le centre de Dakar et celui de Thiès."],
    ["Qu'est-il arrivé à l'ENSET en 2005?", "L'ENSET a été reconstituée en reprenant sa partie industrielle qui était dans l'ESP."],
    ["Quelle transformation a eu lieu en 2006 concernant la division tertiaire de l'ENSUT?", "La division tertiaire devenue Institut Supérieur de Gestion rattachée à la FASEG est revenue dans l'ESP pour constituer son sixième département (Département de gestion)."],
    ["Qu'est-il arrivé à l'ex Centre de Thiès de l'ESP en 2007?", "Il est redevenu l'École Polytechnique de Thiès, rattachée à l'Université de Thiès, puis directement au Ministère chargé de l'Enseignement Supérieur."],
    ["Quelle est la mission de l'École Supérieure Polytechnique (ESP) ?", "La mission de l'École Supérieure Polytechnique (ESP) est de former des techniciens supérieurs, des ingénieurs d'exécution, des managers et des ingénieurs de conception."],
    ["Quelles sont les fonctions préparées par l'ESP ?", "L'ESP prépare aux fonctions dans la production, la recherche appliquée et les services."],
    ["Quels types d'enseignement et d'activités de recherche l'ESP dispense-t-elle ?", "L'ESP dispense un enseignement supérieur et mène des activités de recherche visant au perfectionnement permanent, à l'adaptation et à la participation à l'évolution scientifique et technologique."],
    ["Dans quel cadre l'ESP procède-t-elle à des expertises ?", "L'ESP procède à des expertises dans le cadre de la formation à l'intention des entreprises publiques et privées."],
    ["Quel est l'un des objectifs de l'ESP concernant la communauté ?", "L'un des objectifs de l'ESP est de servir la communauté."],
    ["Dans combien de départements les activités pédagogiques de l'École Supérieure Polytechnique se déroulent-elles ?", "Les activités pédagogiques de l'École Supérieure Polytechnique se déroulent dans six (6) départements."],
    ["Quels sont les départements de l'École Supérieure Polytechnique ?", "Les départements de l'École Supérieure Polytechnique sont : Chimique & Biologie Appliquée, Civil, Électrique, Mécanique, Informatique, et Gestion."],
    ["Quels types de formations l'École Supérieure Polytechnique délivre-t-elle ?", "L'École Supérieure Polytechnique délivre plusieurs formations diplômantes classées en deux grandes catégories."],
    ["Quelles sont les catégories de formations prises en charge par l'État du Sénégal ?", "Les frais de scolarité sont gratuits pour l'étudiant qui y accède par concours au niveau national."],
    ["Quelles sont les catégories de formations prises en charge par un tiers ?", "Les frais de scolarité sont soit pris en charge par l'étudiant, ou par un organisme public ou privé. L'étudiant y accède par test ou sélection de dossier."],
    ["Quels diplômes sont pris en charge par l'État du Sénégal ?", "Diplôme Universitaire de Technologie (DUT), Diplôme d'Ingénieur de Conception (DIC), Diplôme d'Études Supérieures en Commerce, Administration et Finance (DESCAF), Licence en Génie Biomédical, Master de Recherche."],
    ["Quels diplômes sont pris en charge par un tiers ?", "Diplôme d'Ingénieur Technologue (DST), Diplôme d'Ingénieur Technologue (DIT), Diplôme Élémentaire Comptable (DEC), Diplôme Supérieur Comptable (DSC), Licences, Masters."],
    ["Quelle est la note importante à retenir pour les formations prises en charge par un tiers ?", "Dans le cas des formations prises en charge par un tiers, toute année entamée est due, même en cas d'abandon."],
    ["Quelle est l'une des plus prestigieuses écoles d'ingénieur et de management en Afrique francophone?", "L'École supérieure polytechnique (ESP) de l'Université Cheikh Anta Diop de Dakar."],
    ["Quand a été créée l'ESP de Dakar?", "En 1964."],
    ["Combien de diplômés l'ESP a-t-elle formés au moins?", "Plus de 30 000 diplômés."],
    ["Quels types de diplômes l'ESP offre-t-elle?", "Diplôme universitaire de technologie (DUT), diplôme supérieur de technologie (DST), licence, diplôme d'ingénieur technologue (DIT), master, diplôme d'ingénieur de conception (DIC) et doctorat."],
    ["Que présente la troisième édition du catalogue des formations de l'ESP?", "L'ensemble des parcours de formation délivrés dans les six départements de l'ESP, les missions de l'ESP, les différentes formations offertes et les modalités d'admission à ces formations."],
    ["Quelle preuve le document du catalogue de formations fournit-il?", "La preuve que l'offre pédagogique de l'ESP est hautement professionnelle et l'une des plus complètes au Sénégal et en Afrique francophone."],
    ["À quoi sont régulièrement soumises les formations de l'ESP?", "À l'évaluation de l'Autorité nationale d'assurance qualité de l'enseignement supérieur (ANAQ-Sup)."],
    ["Pourquoi les formations de l'ESP sont-elles soumises à l'évaluation de l'ANAQ-Sup?", "Afin de garantir leur qualité, leur pertinence et leur adéquation aux besoins des entreprises et des communautés."],
    ["Quelles sont les missions de l'École Supérieure Polytechnique (ESP) ?", "Former des techniciens supérieurs, des ingénieurs d'exécution, des managers, des ingénieurs de conception ; dispenser un enseignement supérieur et mener des activités de recherche ; organiser des enseignements et des activités de recherche pour le perfectionnement permanent ; procéder à des expertises ; servir la communauté."],
    ["Quels sont les départements de l'École Supérieure Polytechnique (ESP) ?", "Chimique & Biologie Appliquée, Civil, Électrique, Mécanique, Informatique, Gestion."],
    ["Combien de départements propose l'école pour l'excellence ?", "6 départements"],
    ["Quels sont les départements de l'école ?", "Département Génie Chimique et Biologie Appliquée, Département Génie Civil, Département Génie Electrique, Département Génie Mécanique, Département Génie Informatique, Département Gestion"],
    ["Quels sont les types de formations offertes ?", "Formations prises en charge par l'État du Sénégal, Formations prises en charge par un Tiers"],
    ["Quelles sont les formations prises en charge par l'État du Sénégal ?", "Diplôme Universitaire de Technologie (DUT), Diplôme d'Ingénieur de Conception (DIC), Diplôme d'Études Supérieures en Commerce, Administration et Finance (DESCAF), Licence en Génie Biomédical, Master de Recherche"],
    ["Quelles sont les formations prises en charge par un Tiers ?", "Diplôme d'Ingénieur Technologue (DST), Diplôme d'Ingénieur Technologue (DIT), Diplôme Élémentaire Comptable (DEC), Diplôme Supérieur Comptable (DSC), Licences, Masters"],
    ["Que se passe-t-il si une année entamée est abandonnée ?", "Toute année entamée est due, même en cas d'abandon."],
    ["Combien de départements propose l'école pour l'excellence ?", "6 départements"],
    ["Quels sont les départements de l'école ?", "Département Génie Chimique et Biologie Appliquée, Département Génie Civil, Département Génie Electrique, Département Génie Mécanique, Département Génie Informatique, Département Gestion"],
    ["Quels sont les types de formations offertes ?", "Formations prises en charge par l'État du Sénégal, Formations prises en charge par un Tiers"],
    ["Quelles sont les formations prises en charge par l'État du Sénégal ?", "Diplôme Universitaire de Technologie (DUT), Diplôme d'Ingénieur de Conception (DIC), Diplôme d'Études Supérieures en Commerce, Administration et Finance (DESCAF), Licence en Génie Biomédical, Master de Recherche"],
    ["Quelles sont les formations prises en charge par un Tiers ?", "Diplôme d'Ingénieur Technologue (DST), Diplôme d'Ingénieur Technologue (DIT), Diplôme Élémentaire Comptable (DEC), Diplôme Supérieur Comptable (DSC), Licences, Masters"],
    ["Que se passe-t-il si une année entamée est abandonnée ?", "Toute année entamée est due, même en cas d'abandon."],
    ["Quelles sont les modalités pour le dépôt physique pour les élèves en classe de terminale ?", "Fiche de candidature à remplir au niveau de votre établissement, Bulletin de notes du 1er semestre de la classe de Terminale, Bulletins de notes des deux semestres des classes de Première et de Seconde, Cinq mille francs CFA (5 000 F CFA) de frais de dossier non remboursables, Les dossiers, constitués au niveau des établissements, devront être déposés par ces derniers, en un seul envoi, à la scolarité de l'ESP à Dakar"],
    ["Comment se fait le dépôt électronique pour les élèves en classe de terminale ?", "L'inscription et le dépôt en ligne sont possibles via le site web de l'ESP www.esp.sn et sur my.esp.sn"],
    ["Quelles sont les modalités pour le dépôt physique pour les bacheliers ?", "Fiche de candidature disponible à la scolarité ou au CAOSP, Photocopie légalisée de l'attestation du Bac, Photocopie légalisée du relevé de notes du Bac, Bulletins de notes des deux semestres des classes de Seconde, Première et Terminale, Cinq mille francs CFA (5 000 F CFA) de frais de dossier non remboursables, Le dossier complet devra être déposé par l'intéressé(e) à la scolarité de l'ESP à Dakar ou au centre d'orientation régional"],
    ["Comment se fait le dépôt électronique pour les bacheliers ?", "L'inscription et le dépôt en ligne sont possibles via la plateforme concours.esp.sn accessible à partir du site web de l'ESP, Les dates d'inscription au concours DUT sont communiquées par la scolarité de l'ESP. En général dans la période allant de mi-février à mi-mai de chaque année"],
    ["Comment peut on contacter le departement Genie Informatique ?", "Vous pouvez contacter le departement Genie Informatique par mail ou par appel direct. Le mail du departement Genie Informatique est: genie.informatique@esp.sn et leur contact est 00221 33 824 05 40"],
    ["Comment peut on contacter le departement Genie Mecanique ?", "Vous pouvez contacter le departement Genie Mecanique par mail ou par appel direct. Le mail du departement Genie Mecanique est: genie.mecanique@esp.sn et leur contact est 00221 33 824 05 40"],
    ["Comment peut on contacter le departement Genie Electrique ?", "Vous pouvez contacter le departement Genie Electrique par mail ou par appel direct. Le mail du departement Genie Electrique est: genie.electrique@esp.sn et leur contact est 00221 33 824 05 40"],
    ["Comment peut on contacter le departement Genie Civil ?", "Vous pouvez contacter le departement Genie Civil par mail ou par appel direct. Le mail du departement Genie Civil est: genie.civil@esp.sn et leur contact est 00221 33 824 05 40"],
    ["Comment peut on contacter le departement Genie Chimique ?", "Vous pouvez contacter le departement Genie Chimique par mail ou par appel direct. Le mail du departement Genie Chimique est: genie.chimique@esp.sn et leur contact est 00221 33 824 05 40"],
    ["Comment peut on contacter le departement Gestion ?", "Vous pouvez contacter le departement Gestion par mail ou par appel direct. Le mail du departement Gestion est: genie.gestion@esp.sn et leur contact est 00221 33 824 05 40"],
    ["Qui est le chef du departement Genie Informatique ?", "Le chef du departement Genie Informatique est Pr Ibrahima FALL"],
    ["Qui est le chef du departement Genie Mecanique ?", "Le chef du departement Genie Mecanique est M. Ousmane SOW"],
    ["Qui est le chef du departement Genie Electrique ?", "Le chef du departement Genie Informatique est M. Khaly TALL"],
    ["Qui est le chef du departement Genie Civil ?", "Le chef du departement Genie Civil est Libasse SOW"],
    ["Qui est le chef du departement Genie Chimique ?", "Le chef du departement Genie Chimique est M Saidou Moustapha SALL"],
    ["Quelles sont les formations qu'offre le departement genie Mecanique de l'ESP ?", "Les formations qu'offre le departement genie Mecanique de l'ESP sont : Master En Bases Erienne Civile (MBAC), Licence Professionnelle Transport Logistique et Mobilite, Diplome d'Ingenieur Technologue, Diplome Universitaire de Technologie, Licence Professionnelle en Energie Renouvelable, Master de Recherche, Licence Professionnnelle Conducteur des travaux en BTP, Licence Professionnelle en Genie Civil Option Geometre Topographe."],
    ["Quelles sont les formations qu'offre le departement genie Informatique de l'ESP ?", "Les formations qu'offre le departement genie Informatique de l'ESP sont : Licence Genie des Donnees Technologies, Diplome d'Ingenieur de Technologie, Master en Securite et Systeme d'Information, Master en Intelligence Artificielle et Big Data, Master en Securite et Systeme d'Information, Master de Recherche Sciences de l'Ingenieur, Master en Securite et Systeme d'Information, Licence Professionelle et Genie Logiciel, Licence Professionnelle en Systeme, Reseaux "],
    ["Quelles sont les formations qu'offre le departement genie chimique de l'ESP ?", "Les formations qu'offre le departement genie Chimique de l'ESP sont: Diplôme Universitaire de Technologie (DUT) en Génie Chimique : Ce programme est conçu pour les étudiants ayant un niveau Bac+2. Il fournit une base solide en techniques et procédés chimiques. Diplôme Supérieur de Technologie (DST) en Génie Chimique : Un autre programme Bac+2, orienté vers une formation plus spécialisée et technique dans le domaine du génie chimique. Licence (Bac+3) en Génie Chimique : Ce programme de trois ans permet aux étudiants de développer des compétences avancées et une connaissance approfondie des procédés chimiques et des technologies associées. Diplôme d’Ingénieur Technologue (DIT) en Génie Chimique : Ce programme Bac+4 prépare les étudiants à des rôles techniques et de gestion dans l'industrie chimique, combinant des connaissances théoriques et des compétences pratiques. Diplôme d’Ingénieur de Conception (DIC) en Génie Chimique : Ce programme de niveau Bac+5 vise à former des ingénieurs capables de concevoir, optimiser et gérer des procédés chimiques complexes. Master en Génie Chimique : Destiné aux étudiants ayant complété une licence, ce programme de deux ans (Bac+5) se concentre sur des aspects avancés du génie chimique, incluant la recherche et l'innovation."],
    ["Quelles sont les formations qu'offre le departement de gestion de l'ESP ?", "Les formations qu'offre le departement de gestion Civil de l'ESP sont: Diplôme Universitaire de Technologie (DUT) en Génie Civil : Niveau : Bac+2 Durée : 2 ans Diplôme Supérieur de Technologie (DST) en Génie Civil : Niveau : Bac+2 Durée : 2 ans Licence Professionnelle en Génie Civil option Géomètre Topographe : Niveau : Bac+3 Durée : 1 an Contenu : Sciences géographiques, photogrammétrie, télédétection, topographie, DAO, droit foncier, hydraulique, stage professionnel Diplôme d'Ingénieur Technologue (DIT) en Génie Civil : Niveau : Bac+4 Durée : 4 ans Contenu : Mathématiques et sciences physiques, mise à niveau technologique, génie urbain, communication, management, calcul de structures, hydraulique Diplôme d’Ingénieur de Conception (DIC) en Génie Civil : Niveau : Bac+5 Durée : 5 ans"],
    ["Quelles sont les formations qu'offre le departement genie Electrique de l'ESP ?", "Les formations qu'offre le departement genie Electrique de l'ESP sont: "],
    ["Quelles sont les conditions d'admission pour l'ESP ?", "Les conditions d'admission à l'ESP incluent la réussite à un concours d'entrée et la présentation des documents académiques requis."],
    ["Quels sont les frais d'inscription pour les nouveaux étudiants ?", "Les frais d'inscription pour les nouveaux étudiants varient selon le programme, généralement autour de 150 000 FCFA."],
    ["Y a-t-il des résidences universitaires sur le campus ?", "Oui, l'ESP dispose de résidences universitaires pour les étudiants, disponibles sur demande."],
    ["Quels événements culturels sont organisés par l'ESP ?", "L'ESP organise divers événements culturels tels que des journées portes ouvertes, des festivals de musique et des conférences."],
    ["Comment puis-je m'impliquer dans les activités étudiantes ?", "Pour vous impliquer dans les activités étudiantes, rejoignez une association ou participez aux événements organisés par le bureau des affaires étudiantes."],
    ["Quels laboratoires sont disponibles pour les étudiants en ingénierie ?", "L'ESP offre des laboratoires modernes pour la chimie, la physique, l'électronique, et bien d'autres domaines."],
    ["Comment puis-je accéder à la bibliothèque de l'ESP ?", "Pour accéder à la bibliothèque, vous devez être un étudiant ou un membre du personnel de l'ESP et présenter votre carte d'identité."],
    ["Quelles installations sportives sont disponibles sur le campus ?", "Les installations sportives comprennent un terrain de football, des courts de tennis et une salle de sport."],
    ["Y a-t-il des espaces de coworking pour les étudiants ?", "Oui, des espaces de coworking sont disponibles pour les étudiants, équipés de Wi-Fi et d'autres ressources."],
    ["Quels sont les équipements informatiques disponibles pour les étudiants ?", "L'ESP offre des salles informatiques avec des ordinateurs, des imprimantes et des scanners pour les étudiants."],
    ["Quels services de carrière sont offerts par l'ESP ?", "L'ESP propose des services de conseil en carrière, des ateliers de rédaction de CV, et des salons de l'emploi."],
    ["Y a-t-il des programmes de stage disponibles pour les étudiants ?", "Oui, l'ESP offre des programmes de stage en collaboration avec des entreprises locales et internationales."],
    ["Comment puis-je obtenir de l'aide pour la recherche d'emploi ?", "Pour obtenir de l'aide pour la recherche d'emploi, consultez le bureau des carrières de l'ESP."],
    ["Quelles entreprises recrutent des diplômés de l'ESP ?", "De nombreuses entreprises locales et internationales recrutent régulièrement des diplômés de l'ESP."],
    ["Quels sont les taux de placement des diplômés de l'ESP ?", "Les taux de placement des diplômés de l'ESP sont élevés, avec une majorité des diplômés trouvant un emploi dans les six mois suivant l'obtention de leur diplôme."],
    ["Quels événements académiques sont prévus cette année ?", "Les événements académiques incluent des conférences, des ateliers et des séminaires organisés tout au long de l'année."],
    ["Comment puis-je participer aux conférences organisées par l'ESP ?", "Pour participer aux conférences, inscrivez-vous en ligne via le site web de l'ESP ou auprès du bureau des événements."],
    ["Y a-t-il des journées portes ouvertes à l'ESP ?", "Oui, l'ESP organise des journées portes ouvertes deux fois par an pour permettre aux futurs étudiants de visiter le campus."],
    ["Quelles sont les activités de sensibilisation prévues ?", "Les activités de sensibilisation incluent des campagnes sur la santé, la sécurité et l'environnement, organisées par l'ESP."],
    ["Comment puis-je m'inscrire aux ateliers et séminaires ?", "Pour vous inscrire aux ateliers et séminaires, consultez le calendrier des événements sur le site web de l'ESP."],
    ["Quels sont les principaux domaines de recherche à l'ESP ?", "Les principaux domaines de recherche incluent les énergies renouvelables, les matériaux avancés et l'intelligence artificielle."],
    ["Comment puis-je postuler pour un projet de recherche ?", "Pour postuler à un projet de recherche, contactez le département de recherche de l'ESP pour connaître les opportunités disponibles."],
    ["Y a-t-il des collaborations internationales en recherche ?", "Oui, l'ESP collabore avec plusieurs universités et instituts de recherche internationaux."],
    ["Comment puis-je accéder aux publications de recherche de l'ESP ?", "Les publications de recherche sont accessibles via la bibliothèque en ligne de l'ESP."],
    ["Quels sont les laboratoires de recherche disponibles ?", "Les laboratoires de recherche à l'ESP comprennent des installations pour la nanotechnologie, la biotechnologie, et l'ingénierie environnementale."],

    ]

csv_file_path = './data/data_train_extend.csv'

# Écriture des données dans le fichier CSV avec l'encodage UTF-8
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Fichier CSV créé avec succès !")


