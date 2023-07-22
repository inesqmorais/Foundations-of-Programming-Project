

#2.1

#Construtores

def faz_pos(l,c):
    """
    Esta funcao recebe dois argumentos 
    uma linha l e uma coluna c, e devolve um elemento do tipo posicao sendo que
    uma posicao e um tuplo de 2 inteiros nao negativos

    """
    if l==int(l) and l>=0 and c==int(c) and c>=0:
        return (l,c)
    else:
        raise ValueError ("faz_pos: argumentos errados")




#Selectores

def linha_pos(p):
    """
    Esta funcao recebe um argumento do tipo posicao e devolve a linha respectiva
    """
    return p[0]

def coluna_pos(p):
    """
    Esta funcao recebe um argumento do tipo posicao e devolve a coluna respectiva
    """    
    return p[1]
    

#Reconhecedores

def e_pos(arg):
    """
    Esta funcao recebe um argumento e devolve True se o argumento for do tipo 
    posicao e False caso contrario.
    """
    return isinstance(arg,tuple) and len(arg)==2 and int(arg[0])==arg[0] and arg[0]>=0 and int(arg[1])==arg[1] and arg[1]>=0

    
#Testes
def pos_iguais(p1, p2):
    """
    Esta fucao recebe dois argumentos do tipo posicao, p1 e p2, e devolve
    True caso os argumentos correspondam a mesma posicao da chave e False
    caso contrario.
    """
    return p1[0]==p2[0] and p1[1]==p2[1]


#2.2

#Construtores










def verifica_l(l):
    """
    Esta funcao e uma funcao auxiliar da funcao gera_chave_linhas, faz a verificacao do tuplo de 25 letras
    """
    res=()
    for e in l:                       #este ciclo percorre o tuplo e retira as suas repeticoes criando um novo tuplo sem repeticoes
        if e not in res1:
            res=res+(e,)
    return res==l                     #se nao houver repeticoes, ou seja, o novo tuplo for igual ao recebido a verificao do tuplo letras retorna verdadeiro
        

def verifica_mgc(mgc):
    """
    Esta funcao e uma funcao auxiliar da funcao gera_chave_linhas, faz a verificacao da cadeia de caracteres mgc
    """
    cad_aux=''
    for e in mgc:                                        #este ciclo percorre a cadeia de caracteres mgc criando uma nova cadeia de caracteres em que todos os elememtos que nao 
        if ord(e) in range(65,91) or ord(e)==32:         #se encontrem na na lista ascii nas posicoes indicadas sejam eliminados. Estas posicoes da lista ascii referem-se a letras
            cad_aux=cad_aux+e                            #maisculas e espacos
    return cad_aux==mgc                                  #se todas as letras de mgc forem maisculas a verificacao de mgc retorna verdadeiro
 
        
    
def gera_chave_linhas(l, mgc):
    """
    Esta funcao recebe dois argumentos, l e mgc, correspondentes a um tuplo de 25 letras e uma cadeia de caracteres mgc e devolve uma chave. Uma chave consistente numa lista de listas organizada como uma matriz cinco por cinco que recebe a cadeia de caracteres mgc reorganizada de modo a nao conter repeticoes nem espacos seguida do resto das letras contidas no tuplo l
    """
    l_aux1=[]
    l_aux2=[]
    if verifica_l(l) and verifica_mgc(mgc):                                                 #verifica a condicao das letras e da mensagem geracao de codigo
        for i in range(len(mgc)):
            if mgc[i] not in l_aux1 and mgc[i]!=' ':                                        #este ciclo percorre a mgc e retira lhe os espacos bem como as repeticoes criando uma 
                l_aux1=l_aux1+[mgc[i]]                                                      #nova lista 
        for i in range(len(l)):
            if l[i] not in l_aux1:                                                          #este ciclo percorre as letras e adiciona todas as letras nao existentes na mensagem
                l_aux2=l_aux1+[l[i]]                                                        #geracao de codigo a uma nova lista
        l_aux3=l_aux1+l_aux2                                                                #junta as duas listas                                               
        tabela=[l_aux3[0:5],l_aux3[5:10],l_aux3[10:15],l_aux3[15:20],l_aux3[20:25]]         #cria uma matriz cinco pr cinco a chave la dentro
    else:
        raise ValueError("gera_chave_linhas: argumentos errados")
    return tabela

letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
mgc =  "MENSAGEM GERACAO DE CHAVe"




#Selectores

def ref_chave(c, p):
    """
    Esta funcao recebe como argumentos uma chave c e uma posicao p e devolve a
    letra na chave coma posicao p
    """
    return c[p[0]][p[1]]       #retorna a letra da posicao p na chave c sendo
                               #p[0] a linha e p[1] a coluna na chave




#Modificador

def muda_chave(c, p, l):
    """
    Esta funcao recebe como argumentos uma chave c, uma posicao p e uma letra l
    e devolve a chave c com a letra l na posicao p
    """
    c[p[0]][p[1]]=l     #procura a letra na chave com a posicao p e subsitui-a
                        #com a letra l
    return c 




#Reconhecedores

def e_chave(arg):
    """
    Esta funcao verifica se o argumento dado e do tipo chave e retorna True caso seja e Falso caso contrário.
    """
    cad_aux1=''
    cad_aux2=''
    if isinstance(arg,list):                                         #verifica se a chave consiste numa lista
        for linha in arg:                                            #percorre a linhas da lista
            if isinstance(linha,list):                               #verifica se as linhas da lista consistem em listas
                for coluna in linha:                                 #percorre as colunas
                    cad_aux1=cad_aux1+coluna                         #cria uma cadeia de caracteres com os elementos da lista
                    if ord(coluna) in range(65,91):                  #cria uma cadeia de caracteres com os elementos da lista que nao contenham letras
                        cad_aux2=cad_aux2+coluna                     # minusculas(verificacao da chave)               
        return cad_aux2==cad_aux1                                    #retorna verdadeiro se a cadeia de caracteres com os elementos da lista for igual a cadeia de caracteres
    return False                                                     #que contem apenas os elementos da lista que correspondem a letras maiscukas
            



#Transformadores                       
def string_chave(c):
    """
    Esta funcao recebe como argumento uma chave c e devolve uma cadeia de 
    caracteres que uma vez impressa apresenta as letras da cheva c dispostas 
    numa tabela cinco por cinco.

    """
    cad=''
    for linha in range(len(c)):                                                                                                              #corre as linhas
        for coluna in range(0,len(c[linha]),5):                                                                                              #corre as colunas com saltos de 5
            cad=cad+c[linha][coluna]+' '+c[linha][coluna+1]+' '+c[linha][coluna+2]+' '+c[linha][coluna+3]+' '+c[linha][coluna+4] +' '+'\n'
    #por cada coluna adiciona a nova cadeia de caracteres cada letra dessa coluna mais um espaco, adicionando ainda no fim um '\n'    
    return cad


            
    
def digramas(mens):
    msg = ''
    for i in mens:
        if i != ' ':
            msg=msg+i
    lista = []
    while len(msg) > 0:
        if len(msg) != 1 and msg[0] != msg[1]:
            lista += msg[0:2]
            msg = msg[2:]            
        else:
            lista += msg[0] + 'X'
            msg = msg[1:]
            
    return ''.join(lista)


#def digramas(mens):
    #"""
    #Esta funcao recebe como argumento uma cadeia de caracteres  mens, e devolve 
    #uma cadeia de caracteres sem espacos. Se a cadeia de caracteres tiver duas 
    #letras iguais seguidas e inserido um X a seguir a primeira letra repetida
    #deslocando assim toda a mensagem uma posicao para a direita
    #"""
    #cad_aux1=''
    #cad_aux2=''
    #comp=len(mens)-1
    #for i in range(len(mens)):                  #este ciclo percorre a cadeia de caracteres e retira os espacos
        #if mens[i] !=' ':                      
            #cad_aux1=cad_aux1+mens[i]
    #for i in range((len(cad_aux1)-1)):          #este ciclo percorre a nova cadeia de caracteres sem espacos e por cada 
        #if cad_aux1[i]==cad_aux1[i+1]:          #duas letras iguais seguidas adiciona um X entre as duas letras
            #cad_aux2=cad_aux2+cad_aux1[i]+'X'   
        #else:                                   
            #cad_aux2=cad_aux2+cad_aux1[i]
    #cad_aux2=cad_aux2 + mens[comp]              #adiciona a cadeia de caracteres sem letras repetidas a ultima letra    
    #if len(cad_aux2)%2!=0:                      # se a cadeia de caracteres for impar adiciona um X no final da mesma
        #cad_aux2=cad_aux2+'X'    
    #return cad_aux2






def figura(digrm,chave):
    """
    Esta funcao recebe dois argumentos uma cadeia de caracteres 
    com duas letras, digrm, e uma chave e devolve um tuplo de 3 elementos da forma 
    (fig, pos1, pos2) em que fig e a figura determinada pelas letras de digrm, l, c ou r 
    (linha, coluna ou rectangulo) e pos1 e pos2 sao as posicoes ocupadas na chave 
    pela primeira e segunda letra de digrm, respectivamente.
    """
    for linha in range(len(chave)):                     #percorre as linhas
        for coluna in range(len(chave[linha])):         #percorre as colunas
            if digrm[0]==str(chave[linha][coluna]):     # se a primeira letra da cadeia de caracteres que a funcao recebe 
                pos1=(linha,coluna)                     # for igual a uma letra na chave retorna a posicao dessa letra na chave
            if digrm[1]==str(chave[linha][coluna]):     #se a segundaletra da cadeia de caracteres que a funcao recebe 
                pos2=(linha,coluna)                     # for igual a uma letra na chave retorna a posicao dessa letra na chave
    if pos1[0]==pos2[0]:                                 
        fig='l'                               #se a posicao da linha de ambas as letras for igual a figura e l (linha)
    elif pos1[1]==pos2[1]:
        fig='c'                               #se a posicao da coluna de ambas as letras for igual a figura e c (coluna)
    else:
        fig='r'                               #se nem a posicao da linha nem da coluna de ambas letras for igual a figura e r
    return(fig,pos1,pos2)
        
    
    



def codifica_l(pos1,pos2,inc):
    if inc==1:
        
        if pos1[1]==4:
            n_pos1=(pos1[0],0)
        else:
            n_pos1=(pos1[0],pos1[1]+1)  
        if pos2[1]==4:
            n_pos2=(pos2[0],0)
        else:
            n_pos2=(pos2[0],pos2[1]+1)
    else:
        if pos1[1]==0:
            n_pos1=(pos1[0],4)
        else:
            n_pos1=(pos1[0],pos1[1]-1)
        
        if pos2[1]==0:
            n_pos2=(pos2[0],4)
        else:
            n_pos2=(pos2[0],pos2[1]-1)
    return (n_pos1,n_pos2)



def codifica_c(pos1,pos2,inc):
    if inc==1:
        if pos1[0]==4:
            n_pos1=(0,pos1[1])
        else:
            n_pos1=(pos1[0]+1,pos1[1])  
        if pos2[0]==4:
            n_pos2=(0,pos2[1])
        else:
            n_pos2=(pos2[0]+1,pos2[1])
    else:
        if pos1[0]==0:
            n_pos1=(4,pos1[1])
        else:
            n_pos1=(pos1[0]-1,pos1[1])
        
        if pos2[0]==0:
            n_pos2=(4,pos2[1])
        else:
            n_pos2=(pos2[0]-1,pos2[1])
    return (n_pos1,n_pos2)







def codifica_r(pos1,pos2):
    n_pos1=(pos1[0],pos2[1])
    n_pos2=(pos2[0],pos1[1])
    return (n_pos1,n_pos2)




def codifica_digrama(digrm,chave,inc):
    pos_fig=figura(digrm,chave)
    if pos_fig[0]=='l':
        pos_cod=codifica_l(pos_fig[1],pos_fig[2],inc)
    elif pos_fig[0]=='c':
        pos_cod=codifica_c(pos_fig[1],pos_fig[2],inc)
    else:
        pos_cod=codifica_r(pos_fig[1],pos_fig[2])
    cad_cod=chave[pos_cod[0][0]][pos_cod[0][1]]+chave[pos_cod[1][0]][pos_cod[1][1]]
    return cad_cod
        
        
def codifica(mens,chave,inc):
    cad_cod1=''
    digrm=digramas(mens)
    for i in range(0,len(digrm)-1,2):
        cad_cod1=cad_cod1 + codifica_digrama(digrm[i] + digrm[i+1],chave,inc)
    return cad_cod1






    
    
  
        
        
        
    
        
    
        
    
        
    
    
        
        
        
    
        
    
        
        
       

    
                
    
                         
    
        
        


