#include <stdio.h>

int main() {
 
    int q, d, p, paginas;

    while(scanf("%d", &q) != 0){
        if(q==0){
            break;
        }
        scanf("%d %d", &d, &p);
        paginas= (q*d*p)/(p-q);

        if(paginas > 1){
            printf("%d paginas\n", paginas);
        }
        else{
            printf("%d pagina\n", paginas);
        }
    }
 
    return 0;
}