%predicados
homem(herb_simpson).
homem(homer_simpson).
homem(abe_simpson).
homem(bart_simpson).
homem(clancy_bouvier).
mulher(mona_simpson).
mulher(lisa_simpson).
mulher(maggie_simpson).
mulher(jacqueline_bouvier).
mulher(marge_bouvier).
mulher(patty_bouvier).
mulher(selma_bouvier).
mulher(ling_bouvier).
filho(bart_simpson,homer_simpson).
filho(lisa_simpson,homer_simpson).
filho(maggie_simpson,homer_simpson).
filho(bart_simpson,marge_bouvier).
filho(lisa_simpson,marge_bouvier).
filho(maggie_simpson,marge_bouvier).
filho(homer_simpson,abe_simpson).
filho(homer_simpson,mona_simpson).
filho(herb_simpson,abe_simpson).
filho(herb_simpson,mona_simpson).
filho(marge_bouvier,clancy_bouvier).
filho(marge_bouvier,jacqueline_bouvier).
filho(selma_bouvier,clancy_bouvier).
filho(selma_bouvier,jacqueline_bouvier).
filho(patty_bouvier,clancy_bouvier).
filho(patty_bouvier,jacqueline_bouvier).
filho(ling_bouvier,selma_bouvier).
casado(homer_simpson,marge_bouvier).
casado(marge_bouvier,homer_simpson).
casado(abe_simpson,mona_simpson).
casado(mona_simpson,abe_simpson).
casado(clancy_bouvier,jacqueline_bouvier).
casado(jacqueline_bouvier,clancy_bouvier).

%regras
%irmao(X,Y):- filho(X,Z),filho(Y,Z).
irma(X,Y):- mulher(X), (  filho(X,Z), filho(Y,Z) ).
irmao(X,Y):- homem(X),  (  filho(X,Z), filho(Y,Z) ).
tio(X,Y):- homem(X),( ( (   irmao(X,Z) ,(X\=Z))  ,filho(Y,Z) ) ; ( casado(X,Z),(irmao(Z,J);irma(Z,J)),(Z\=J),filho(Y,J) ) ).
tia(X,Y):- mulher(X),( ( (   irma(X,Z),(X\=Z)),filho(Y,Z) ); ( casado(X,Z),(irmao(Z,J);irma(Z,J)),(Z\=J),filho(Y,J) ) ).
prima(X,Y):- mulher(X),(  (tia(Z,X);tio(Z,X) ), filho(Y,Z) ).
primo(X,Y):- homem(X), (  (tia(Z,X);tio(Z,X) ), filho(Y,Z) ).
avô(X,Y):- homem(X), ( filho(Y,Z),filho(Z,X)  ).
avó(X,Y):- mulher(X), ( filho(Y,Z),filho(Z,X)  ).
pai(X,Y):- homem(X), (  filho(Y,X)  ).
mae(X,Y):- mulher(X), (  filho(Y,X)  ).






