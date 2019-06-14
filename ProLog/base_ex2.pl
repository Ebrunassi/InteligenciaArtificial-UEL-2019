%predicados
e_um(atacante,atleta).
e_um(atleta,pessoa).
e_um(basquete_3x3,esporte_olimpico).
e_um(basquete,esporte_olimpico).
e_um(chuteira,tenis).
e_um(esporte_olimpico,esporte).
e_um(futebol,esporte_olimpico).
e_um(futsal,esporte).
e_um(neymar,atacante).
e_um(oscar,atacante).
e_um(tenis,calcado).
e_um(tite,tecnico).
tem(atleta,calcado).
tem(calcado,sola).
tem(neymar,chuteira).
tem(esporte,atividade_fisica).
tem(esporte,tecnico).
tem(pernas,pes).
tem(pessoa,braco).
tem(pessoa,cabeca).
tem(pessoa,pernas).
tem(pes,pe).
tem(pe,unha).
tem(selecao_brasileira,neymar).
tem(selecao_brasileira,oscar).
tem(selecao_brasileira,tite).

%regras
e_um_recursivo(X,Y):- e_um(X,Y).
e_um_recursivo(X,Y):- e_um(X,Z), e_um_recursivo(Z,Y).

tem_recursivo(X,Y):- (tem(X,Z); e_um(X,Z)) , tem_recursivo_2(Z,Y).
tem_recursivo(X,Y):- ( ( tem(X,Z) ; e_um(X,Z) ) , tem_recursivo(Z,Y)) ; tem_recursivo_2(X,Y).
tem_recursivo_2(X,Y):- tem(X,Y).
tem_recursivo_2(X,Y):- tem(X,Z) , tem_recursivo_2(Z,Y).







