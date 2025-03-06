# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define papaChar = Character(_("Papa"), color ="#1679ca" )
define ma = Character(_("Voz misteriosa"), color= "#f6ff00")
define pitagorasChar = Character(_("pitagoras"), color= "#09e4059d")
define v = Character(_("Você"), color = "#ff00009d")
define m = Character(_("Maestro"), color= "#f6ff00")
define guidoChar = Character(_("Guido"), color = "#ff0077")
define paganiniChar = Character(_("Paganini"), color = "#ff5900ff")
define luciferChar = Character(_("Demonio"), color = "#a1baffff")
image black = "#000"



define gr = False 
define me = False
define re = False
define ba = False
define mo = False
define cont = 0
define contNotas = 0
define do = 0
define re= 0
define mi= 0
define fa= 0
define sol = 0
define la = 0
define si = 0
define minigame = True
define biblio = False  #####mudar para false
define tentativagr =0
define tentativame =0
define tentativabiblio =0
define tentativadiabo =0
define badges = 0 ###Mudar para 0



# The game starts here.

label start:
    
    play music "grecia.mp3" volume 0.05 fadein 0.5
    scene biblioteca
    with fade
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #colocar musica tensa.
    ma "Olá, visitante"
    show bsurpreso at right
    v "Quem está ai?"
    
    show goh_defa1 at left
    m "Me chamo Maestro,Estou aqui para te mostrar uma das maravilhas da matemática,"
    
    hide bsurpreso
    show boy4 at right
    v"maravilha da matematica?"
    
    hide goh_defa1
    show goh_hohoemia1 at left
    m "Sim, uma maravilha da matematica, a musica"
    
    hide goh_defa1
    hide boy4
    show bsurpreso at right
    v "Musica? mas o que a musica tem a ver com matematica?"
    hide bsurpreso
    hide goh_hohoemia1
    show goh_omakasea2 at center
    m"É isso que iremos descobrir, Irei te levar a momentos importantes e incriveis da historia da música"
    m"Aonde descobriremos da onde surgiram as coisas que conhecemos hoje."
    m"Viajaremos para a grécia antiga, idade média, renascimento até a era moderna, apredendo coisas novas e interessante sobre a musica. "
    m"Para qual era deseja viajar? com meu equipamento de Realidade aumentada, podemos viajar para qualquer momento importante para a musica."
    m"então..."
    

    jump escolha
    

label escolha:
    m"Para onde deseja viajar?"
    menu:
        "Grecia antiga":
            
            jump grecia

        "Idade média":
            jump media
        
        "Biblioteca":
            jump biblioFinal
        
        "Desafio Final":
            jump diabo

          

label grecia:
    $ gr = True
    $ tentativagr = tentativagr + 1
    hide goh_omakasea2
    stop music fadeout 1.0
    scene portal
    with fade
    "..."
    play sound "tp.mp3" volume 0.05
    play music "atena.mp3" volume 0.05
    
    scene atenas
    with fade
    show bsurpreso at right
    with fade
    v"Uau, que incrivel..."
    hide bsurpreso
    show boy1 at right
    v"Parece tão real..."
    hide boy1
    show b1 at right
    "..."
    v"Quem é aquele?"
    
    show goh_omakasea2 at left
    m"HAHAHA!"
    m"Aquele rapaz, é pitagoras, o pai da matematica e da musica."
    
    hide b1 
    show bsurpreso at right
    v"Pitagoras?"
    hide bsurpreso
    hide goh_omakasea2
    show pinormal
    with fade
    pitagorasChar"Estavam falando de mim?"
    pitagorasChar"Falando nisso..."
    pitagorasChar"Que vestes estranhas, de qual região estão vindo?"
    hide pinormal
    show bsurpreso at left
    "..."
    show pinormal at right
    pitagorasChar"Bom, não importa."
    pitagorasChar"Quero que vejam o que descobri"
    hide bsurpreso
    show goh_omakasea2 at left
    m"Por que não? nos mostre o que descobriu!"
    hide goh_omakasea2
    show pinormal
    pitagorasChar"Me acompanhem"
    menu:
        "acompanhar":
            
            scene 100hz1
            with fade
            show pinormal at right
            pitagorasChar"Reparem está corda..."
            pitagorasChar"Quando a estico, e passo o dedo sobre ela, ela produz um som"
            play sound "oitava1.mp3"
            "..."
            pitagorasChar"Agora divida ela ao meio novamente e toque-a "
            scene 100hz2
            with fade
            "..."
            scene 200hz1
            with fade
            show pinormal at right
            pitagorasChar"este é o resultado dividindo a corda ao meio."
            pitagorasChar"vamos toca-la"
            play sound "oitava2.mp3"
            "..."
            pitagorasChar"Ouviram?"
            pitagorasChar"É mesma nota, so que mais aguda, ou seja"
            pitagorasChar"Uma oitava acima."
            pitagorasChar"Se pegarmos esta metade que tinhamos, e dividirmos ela novamente ao meio"
            scene 200hz2
            with fade
            show pinormal at right
            "..."
            scene 400hz
            with fade
            show pinormal at right
            pitagorasChar"Teremos outra oitava, a mesma nota inicial so que ainda mais aguda."

            play sound "oitava3.mp3"
            "..."
            pitagorasChar"Incrivel não?"
            pitagorasChar"Quando temos a mesma nota so que mais aguda, dizemos que ela está uma oitava acima."
            pitagorasChar"Quando temos a mesma nota so que mais grave, dizemos que ela está uma oitava abaixo."
            pitagorasChar"Vamos testar seu ouvido?"
            hide pinormal
            scene atenas
            show bsurpreso
            v"Testar meu ouvido?"
            hide bsurpreso
            show pinormal
    
            pitagorasChar"Isso, preste atenção, irei tocar duas notas iguais, so que uma mais grave(grossa) e outra mais fina (aguda)"
            pitagorasChar"e quero que me diga se está uma oitava acima ou uma oitava baixo, utilizando o conceito que expliquei agora a pouco"
            pitagorasChar"pronto?"
            
            jump oitavas
            label oitavas:
                
                play sound oitavas
            "A segunda nota está uma oitava acima ou abaixo?"
            menu:   
                "Tocar novamente":
                    jump oitavas

                "uma oitava acima":
                    pitagorasChar"Isso mesmo, como a segunda nota é a mesma mais aguda(fina), ela es´ta uma oitava acima"
                    pitagorasChar"Então podemos notar que a oitava está em uma razão de 2 para 1"
                    pitagorasChar"logo, podemos encontrar outras notas musicais dividindo a corda em outras regiões."
                    pitagorasChar"Assim descobri as notas musicais"
                    pitagorasChar"Bom, tenho que voltar aos meus afazeres, passar bem, amigos"
                    hide pinormal
                    show pnormal 
                    if tentativagr ==1:
                        play sound "conquista.mp3"
                        m"Parabéns, você acertou de primeira, pegue isto, uma insigna musical, caso colete todas, receberá uma recompensa ao final."
                        m"Vamos para a proxima aventura!"
                        $ badges = badges+1
                        "You hit [badges]"
                        jump escolha
                        
                    else:
                        m"Correto, você acertou!"
                        m"Bom, acho que ja vimos o suficiente, vamos voltar"
                        hide pnormal
                        show pnormal at right
                        show bsurpreso at left
                        v"mas já?"
                        m"temos mais historias para ver, garoto, vamos"
                        jump escolha

                "uma oitava abaixo":
                    pitagorasChar"Creio que você se confundiu, vamos novamente"
                    $ tentativagr = tentativagr+1
                    jump oitavas
                
        "não acompanhar":
            $ cont = 1
            pitagorasChar"Ok, irei, continuar meu trabalho. Adeus."
            hide pinormal
            "Você perdeu uma importante explicação de pitágoras sobre as notas musicais."
            show pnormal 
           # m"Bom, acho que ja vimos o suficiente, vamos voltar"
            #hide pnormal
            #show pnormal at right
            #show bsurpreso at left
            #v"mas já?"
            #v"temos mais historias para ver, garoto, vamos"
                    
            jump oitavas


label media:

    
    hide pnormal
    hide bsurpreso
    if gr!=True:
        show pnormal
        m"Acho que ainda não estamos prontos para está historia, vamos ver a anterior"
        jump escolha 
    
    $ me = True
    $ do = 0
    $ tentativame = tentativame+1

    stop music fadeout 1.0
    scene portal
    with fade
    play sound "tp.mp3" volume 0.05
    "..."
    play music "cantoGregoriano.mp3" volume 0.05
    
    scene igreja2
    with Dissolve(1.0)
    show bsurpreso
    v"Uma igreja!?"
    hide bsurpreso
    show boy1 
    v"Estamos na idade média, mas em que ano?"
    hide boy1
    show boy1 at right
    show pnormal at left
    m"Se não me engano, no seculo..."
    hide boy1
    hide pnormal
    show papa
    papaChar"Seculo X, meus filhos"
    papaChar"Não parecem ser daqui..."
    papaChar"Então me apresentarei, Sou Bento, O oitavo de meu nome, atual papa do sacro emperio romano"
    hide papa
    show bsurpreso 
    play sound "livroCaindo.mp3"
    v"P-Papa?"
    hide bsurpreso
    "BARULHO DE ALGO CAINDO NO CHÃO"
    show papab 
    papaChar"Guido, que bagunça é essa? Quanta papelada..."
    hide papab
    stop sound
    show guido
    guidoChar"Mil perdões, meu senhor, estou prestes a concluir um estudo sobre a notação das notas musicais"
    hide guido
    show guido at left
    show papa at right
    papaChar"Notação musical? estudo? Conte-me mais..."
    guidoChar"Convido-os à minha sala de estudos."
    menu:
        "acompanhar":
            show black 
            with dissolve
            play sound "doorOpen.mp3"

            jump quartoGuido
        "Não acompanhar":
            if cont <= 1:
                $ cont = cont + 1
                "Seu objetivo agora é dizer em ordem as notas musicais"
                hide guido
                hide papa
                jump testeNotas
    label quartoGuido:
        scene quarto
        with Dissolve (5)
        stop sound 
        hide guido
        hide papa
        show guido 
        guidoChar"Perdoem pela a bagunça..."
        hide guido
        show guido at left
        show papa at right
        papaChar"N se preocupe, guido, mas nos explique logo o que vc tem em mente"
        guidoChar"Certo, meu senhor...!"
        hide papa
        hide guido
        show guido
        guidoChar"Bem, como sabem, sou responsavel pelo ensinamento de instrumentos da nossa região"
        guidoChar"Entretanto, estou cansado de ter que explicar as notas da mesma forma toda vez..."
        guidoChar"""A bolinha entre a segunda linha, a bolinha na quarta linha..."""
        guidoChar"Isso demanda muito tempo e é cansativo."
        guidoChar"Recentemente em meus aposentos estava estudando o canto liturgico ut queant laxis em homenagem a São João Batista"
        guidoChar"E pensei que poderia nomear cada nota musical, sendo assim mais facil e intuitivo de explicar aos alunos ao invés de dizer a posição delas."
        guidoChar"Mas não sei como nomealas..."
        hide guido
        show papa 
        papaChar"HM... Uma ideia interessante, guido!"
        papaChar"Estava ouvindo o canto liturgico de São João Batista, certo?"
        papaChar"E se em homenagem a este canto, nomearmos as notas retirando-as das letras iniciais do canto?"
        hide papa 
        show guido 
        guidoChar"Se não me engano o canto é o seguinte:"
        "{b}UT{/b} queant laxis"
        "{b}RE{/b}sonare fibris,"
        "{b}MI{/b}ra gestorum,"
        "{b}FA{/b}muli tuorum,"
        "{b}SOL{/b}ve polluti,"
        "{b}LA{/b}bii reatum"
        "{b}SA{/b}ncte Ioannes"
        "..."
        guidoChar"{b}Ut, Re, Mi, Fa, Sol La, Si...{/b}"
        guidoChar"Perfeito, senhor, Creio que isso funcionará mais do que o esperado."
        guidoChar"Voltarei aos meus estudos, senhores"
        hide guido
        show pnormal
        m"Foi assim que o nome das notas musicais foram criados"
        m"Ao longo dos anos a palavra {b}UT{/b} foi trocada por {b}DÓ{/b}"
        m"Não se sabe ao certo como isso ocorreu, ouvi historia que dizem que foi o rei Dominos que trocou em sua propia homenagem."
        m"Vamos ver se conseguiu aprender, jovem"
        label testeNotas:
            
        menu:

            "RE":
                if do == 1:
                    $ do = do+1
                    play sound "D.mp3"
                    jump testeNotas
                else:
                    "Voce errou, comece novamente!"
                    $ do = 0
                    $ tentativame = tentativame+1
                    jump testeNotas



            
            "DO":
                if do <= 0:
                    $ do = do+1
                    play sound "C.mp3"
                    jump testeNotas
                else:
                    "Você errou, comece novamente!"
                    $ tentativame = tentativame+1
                    $ do = 0
                    jump testeNotas


            "SOL":
                if do == 4:
                    $ do = do+1
                    play sound "G.mp3"
                    
                    jump testeNotas
                else:
                    "Voce errou, comece novamente!"
                    $ tentativame = tentativame+1
                    $ do = 0
                    jump testeNotas


            "LA":
                if do == 5:
                    $ do = do+1
                    play sound "A.mp3"
                    
                    jump testeNotas
                else:
                    "Voce errou, comece novamente!"
                    $ tentativame = tentativame+1
                    $ do = 0
                    jump testeNotas




            "MI":
                if do == 2:
                    $ do = do+1
                    play sound "E.mp3"
                    jump testeNotas
                else:
                    "Voce errou, comece novamente!"
                    $ tentativame = tentativame+1
                    $ do = 0
                    jump testeNotas


            "SI":
                if do == 6:
                    $ do = do+1
                    play sound "B.mp3"
                    if tentativame ==1:
                        play sound "conquista.mp3"
                        m "Você acertou sem errar, parabéns, você recebeu outra insigna da musica!"
                        $ badges = badges+1
                        "You hit [badges]"
                        jump finalmedia
                        
                    else:
                        "Você acertou, Parabéns!"
                        jump finalmedia

                else:
                    "Voce errou, comece novamente!"
                    $ tentativame = tentativame+1
                    $ do = 0
                    jump testeNotas



            "FA":
                if do == 3:
                    $ do = do+1
                    play sound "F.mp3"
                    jump testeNotas
                else:
                    "Voce errou, comece novamente!"
                    $ tentativame = tentativame+1
                    $ do = 0
                    jump testeNotas


    label finalmedia:
        show pnormal
        m"Vejo que já aparendeu a notação de guido, ela é muito importante no nosso tempo"
        m"Graças ao guido, as notas receberam nomes, ele também é o criador da pauta musical que usamos hoje em dia!"
        m"Podemos dizer que ele revolucionou à forma como a musica é passada, compartilhada e escrita."
        m "para onde deseja viajar?"
        menu:
            "grecia":
                jump grecia
            "media":
                jump media
            "biblioteca":
                jump biblioFinal
            "dDesafio Final":
                jump diabo
       




label biblioFinal:
    
    if me!=True:
        show pnormal
        m"Acho que ainda não estamos prontos para está historia, vamos ver a anterior"
        jump escolha
    $ biblio = True
    hide pnormal 
    scene portal
    stop music
    play sound "tp.mp3" volume 0.05
    "..." 
    play music "grecia.mp3" volume 0.05 fadein 0.5
    scene biblioteca
    with fade
    show pnormal 
    m"Parece que é a minha vez de te ensinar algo."
    m"Toda essa viagem teve um proposito!"
    m"Te preparar para o conhecimento de acordes e harmonia musical!"
    hide pnormal
    show bsurpreso
    v"A-acordes?"
    hide bsurpreso  
    show pnormal
    m"Isso, acordes."
    m"Acordes são a base da harmonia musical."
    m"Eles são a junção de 3 ou mais notas que são harmonicas entre elas"
    m"Ou seja, se combinam, agradam aos ouvidos."
    m"Os tipos de acordes mais comuns são as {b} Triades e Tetrades {/b}"
    m"Consegue me dizer a diferença entre eles?"
    menu:
        "Sim":
            menu:
                "Tetrades possuem 3 notas na formação do acorde e as triades mais de 3":
                    "Está incorreto, irei te explicar!"
                    jump explicarTetra
                
                "Triades possuem 3 notas na formação do acorde e as tetrades possuem 4 notas":
                    m"Perfeito!"
                    jump explicarForma
        "Não": 
            label explicarTetra:
                m"Como havia dito, acordes são formados de 3 ou mais notas!"
                m"Uma Triade, possui apenas 3 notas!, Já  as tetrades possuem 4 notas."
    label explicarForma:
        m"Com esses conhecimentos, irei te explicar agora como formar um acorde Triade e Tetrade."
        m"Lembra-se que aprendemos as notas {b}DO, RE, MI, FA, SOL, LA, SI?{/b}"
        m"Denominamos a primeira nota de {b}Tônica ou Fundamental{/b} Ela que sera responsavel pelo nome do acorde!"
        m"a segunda nota, denominamos de segunda, e assim sussetivamente até a ultima nota, que chamamos de sétima!"
        m"Uma TRIADE é formada pela Primeira, terça e quinta nota."
        m"Logo, 3 notas."
        m"Com a tetrade funciona da mesma maneira, entretanto, adicionamos a Setima nota, assim, totalizando 4 notas."
    label exemploo:
        m"Darei um exemplo."
        m"Se pegarmos a escala de dó {b}DO, RE, MI, FA, SOL, LA, SI?{/b} e tentarmos descobrir o acorde de SOL"
        m"A primeira nota sera o sol, pois é ele quem da o nome do acorde"
        m"A terca de SOL, sera SI"
        m"e a quinta de SOL será RÉ"
        m"Assim teremos as notas DO RE MI FA {b}SOL(TONICA){/b}, LA, {b}SI (TERÇA){/b}, DO {b}RÉ (QUINTA){/b}"
        m"Gostaria que eu explicasse novamente a formação de acordes"
        menu: 
            "sim":
                jump exemploo
            "não":
                m"Gostaria que montasse para mim o Acorde Triade de DÓ, lembrando que o acorde é formado pela Tonica, Terça e Quinta"
                jump resetVariavel

    
    label resetVariavel:
    # "Variaveis zeradas"
        $ do = 0
        $ re = 0
        $ la = 0
        $ si = 0
        $ mi = 0
        $ sol = 0
        $ fa = 0
        $ contNotas = 0

        if minigame == True:
        #  "Retornando ao minigame"
            jump minigameNotas
        else:
        #    "entrou no else"
            "Agora quero a triade de FA"
            jump minigameNotas2
        
    label minigameNotas:
        
        
        menu:
            
            "DO":
                
                if do <= 0:
                    $ contNotas = contNotas+1
                    $ do = do+1
                    play sound "C.mp3"
                    if contNotas==3:
                        if do == 1 and mi == 1 and sol == 1:
                            $ minigame = False
                            "Você Acertou!"
                            play sound "acordeC.mp3"
                            "Este é o acorde de Dó MAIOR"
                            "Agora vamos para a proxima!"
                            
                            
                            
                            jump resetVariavel
                        else:
                            "Você Errou!"
                            jump resetVariavel
                    else:
                        jump minigameNotas
                else:
                    "Essa nota ja foi pressionada"
                    jump minigameNotas

            "RE":
                if re == 0:
                    $ re = re+1
                    $ contNotas = contNotas+1
                    play sound "D.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas
                
                                
            "MI":
                if mi <= 0:
                    $ contNotas = contNotas+1
                    $ mi = mi+1
                    play sound "E.mp3"
                    if contNotas==3:
                        if do == 1 and mi == 1 and sol == 1:
                            $ minigame = False
                            "Você Acertou!"
                            play sound "acordeC.mp3"
                            "Este é o acorde de Dó MAIOR"
                            "Agora vamos para a proxima!"
                            
                            jump resetVariavel
                        else:
                            "Voce errou!"
                            jump resetVariavel
                    else:
                        jump minigameNotas
                else:
                    "Essa nota ja foi pressionada"
                    jump minigameNotas
            "FA":
                if fa <= 0:
                    $ fa = fa+1
                    $ contNotas = contNotas+1
                    play sound "F.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas
            "SOL":
                if sol <= 0:
                    $ contNotas = contNotas+1
                    $ sol = sol+1
                    play sound "G.mp3"
                    if contNotas==3:
                        if do == 1 and mi == 1 and sol == 1:
                            $ minigame = False
                            "Você Acertou!"
                            play sound "acordeC.mp3"
                            "Este é o acorde de Dó MAIOR"
                            "Agora vamos para a proxima!"
                            
                            jump resetVariavel
                        else:
                            "Voce errou!"
                            jump resetVariavel

                    else:
                        jump minigameNotas
                else:
                    "Essa nota ja foi pressionada"
                    jump minigameNotas
            "LA":
                if la <= 0:
                    $ la = la+1
                    $ contNotas = contNotas+1
                    play sound "A.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas
            "SI":
                if si <= 0:
                    $ si = si+1
                    $ contNotas = contNotas+1
                    play sound "B.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas


    label minigameNotas2:
        
        menu:
            "DO":
                
                if do <= 0:
                    $ contNotas = contNotas+1
                    $ do = do+1
                    play sound "C.mp3"
                    if contNotas==3:
                        if fa == 1 and la == 1 and do == 1:
                            "Você Acertou!"
                            play sound "acordeG.mp3"
                            "Esse é o acorde de FA MAIOR"
                            $ minigame = False
                            jump menuu
                        else:
                            "Você Errou!"
                            jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Essa nota ja foi pressionada"
                    jump minigameNotas2

            "RE":
                if re <= 0:
                    $ contNotas = contNotas+1
                    play sound "D.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas2
                
                                
            "MI":
                if mi <= 0:
                    $ contNotas = contNotas+1
                    stop sound
                    play sound "E.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas2
            "FA":
                if fa <= 0:
                    $ contNotas = contNotas+1
                    $ fa = fa+1
                    play sound "F.mp3"
                    if contNotas==3:
                        if fa == 1 and la == 1 and do== 1:
                            "Você Acertou!"
                            play sound "acordeG.mp3"
                            "Esse é o acorde de FA MAIOR"
                            $ minigame = False
                            jump menuu
                        else:
                            "Você Errou!"
                            jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Essa nota ja foi pressionada"
                    jump minigameNotas2
            "SOL":
                if sol <= 0:
                    $ contNotas = contNotas+1
                    play sound "G.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas2
            "LA":
                if la <= 0:
                    $ contNotas = contNotas+1
                    $ la = la+1
                    play sound "A.mp3"
                    if contNotas==3:
                        if fa == 1 and la == 1 and do== 1:
                            "Você Acertou!"
                            play sound "acordeG.mp3"
                            "Esse é o acorde de FA MAIOR"
                            $ minigame = False
                            jump menuu
                        else:
                            "Você Errou!"
                            jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Essa nota ja foi pressionada"
                    jump minigameNotas2
            "SI":
                if si <= 0:
                    $ contNotas = contNotas+1
                    play sound "B.mp3"
                    if contNotas ==3:
                        "Incorreto, Vamos começar de novo!!"
                        jump resetVariavel
                    else:
                        jump minigameNotas2
                else:
                    "Você ja pressionou essa nota!"
                    jump minigameNotas2           
label menuu:
        menu:
            "grecia":
                jump grecia
            "media":
                jump media
            "biblioteca":
                jump biblioFinal
            "Desafio Final":
                jump diabo  
label diabo:
    if biblio!=True:
        show pnormal
        m"Acho que ainda não estamos prontos para está historia, vamos ver a anterior"
        jump escolha
    hide pnormal
    scene biblioteca
    show panger
    stop music
    play music "tensao.mp3"
    play sound "pedraCaindo.mp3"
    m"O QUE ESTÁ ACONTECENDO? PARECE QUE O DISPOSITIVO DEU PROBLEMA..."
    hide panger
    show panger at left
    show bsurpreso at right
    v"Como assim problema?"
    m"Eu não sei, isso nunca tinha acontecido antes"
    hide panger
    hide bsurpreso
    
    play sound "scream.mp3"
    scene black 
    with Dissolve (5)
    stop sound
    scene quartopaga
    with Dissolve(2)
    v"Quem é aquele deitado?"
    m"Não tenho certeza, mas me parece ser paganini... "
    v"Paganini?"
    m"a historia de paganini é rodeada por muitos mitos e lendas"
    m"Vamos observar com o que ele está sonhando..."
    hide panger
    hide bsurpreso

    scene black
    with Dissolve(3)
    show paganini
    paganiniChar"Aonde estou? que breu é esse?"
    paganiniChar"Quem está ai? consigo ouvir sua respiração"
    hide paganiniChar
    "Vejo que tem bons sentido, paganini"
    hide paganini
    show luciferr
    with Dissolve(2)
    hide luciferChar
    show luciferr at left
    show paganini at right
    paganiniChar"Quem é você? Como entrou aqui?"
    luciferChar"Paganini, tenho te ouvido tocar violino a muito tempo."
    luciferChar"Devo admitir que você possui habilidades incriveis"
    luciferChar"Tenho um dever para você cumprir"
    paganiniChar"Dever?"
    luciferChar"Exato, quero que espalhe minha musica para o mundo."
    luciferChar"Me de seu violino."
    hide luciferr
    stop music
    show luciferviolin at left
    with Dissolve(2)
    
    
    play music "Thoughts.mp3"
    hide luciferviolin 
    with Dissolve(5)
   # with Dissolve(5)
    scene quartopaga
    with Dissolve(3)
    show paganini
    paganiniChar"Foi tudo um sonho? Quem som era aquele..."
    paganiniChar"Nunca tinha ouvido nada igual a aquilo"
    paganiniChar"Preciso do meu violino para tentar reproduzir"
    paganiniChar"Quem são vocês?"
    hide paganini
    show pnormal
    m"somos visitantes, fomos trazidos para cá."
    hide pnormal
    show paganini
    paganiniChar"Trazido por quem?"
    hide paganini
    "Por mim..."
    
    show luciferr
    with Dissolve(2)
    luciferChar"Vocês 3 serão desafiados a reproduzir a minha musica."
    luciferChar"Este será o desafio de vocês."
    luciferChar"O perdedor será preso para sempre na linha temporal, vagando para sempre e sem destino"
    luciferChar" Estão prontos?"
    hide luciferr

    stop music
    jump guitarHero

label guitarHero:

    window hide

    # define the song titles and their files
    python:
        import os
        audio_map = {
            'Thoughts': (
                'audio/Thoughts.mp3',
                'audio/Thoughts.beatmap.txt'
                )
        }
        
        # use a menu
        choice = renpy.display_menu(list(audio_map.items()))

    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    # unpack the file paths associated with the chosen song
    $ audio_path, beatmap_path = choice
    call screen rhythm_game(audio_path, beatmap_path, beatmap_stride=1)

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return
    "You hit [num_hits] notes out of [num_notes]."

    if num_hits <= 200:
        jump finalPessimo
    else:
        jump fim

label finalPessimo:
    scene black 
    with Dissolve(1)
    show luciferChar
    with Dissolve(2)
    "Você foi aprisionado no tempo, não pertencendo a lugar algum, vagando sem rumo e sem proposito."
    "FIM"
    return 
label fim:
    "You hit [badges]"
    if badges >=2:
        window hide
        scene black 
        with Dissolve(3)
        "Você se tornou um artista renomado na area da musica."
        "Suas composições se tornarão inesqueciveis e conhecidas mundialmente"
        "Parabéns, Completou o jogo pelo melhor caminho!"
        return
    if badges < 2 :
        scene black 
        with Dissolve(3)
        "Espero que tenha conhecido aprender algo e isso tenha agregado algo para você!"
        "Foi uma aventura e tanto. Mas ainda há muito mais a se aprender com a musica!"
        "Espero ve-lo novamente"
        "Obrigado!"
        return 


   
