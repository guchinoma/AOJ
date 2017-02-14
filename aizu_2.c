// This function dealing with bubble sort
int bubble_sort(int list){
    int j;
    for(j=0; j<10; j++){
        int k;
        for(k=0; k<9; k++){
            if(list[k]>list[k+1]):
                int tmp = list[k+1];
                list[k+1] = list[k];
                list[k] = tmp;
        }
    }
}

int main(){
    int array[9];
    int i;
    for(i=0; i<10; i++){
        scanf("%d", &array[i]);
    }
    bubble_sort(array);
    return 0;
}