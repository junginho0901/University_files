#include<stdio.h>
#include<math.h>

int main()
{
    printf("마술카드\n");
    int numbers_of_card = 0;
    printf("카드의 개수를 입력하세요:");
    scanf("%d", &numbers_of_card);

    

    int array[14][16384] = { 0 };

    int biggest_Number = pow(2, numbers_of_card);//카드내의 최대값
    printf("1부터 %d 사이까지 숫자 중 한 숫자를 생각해주세요.준비가 돼셨다면 엔터를 눌러주세요.\n",biggest_Number-1);
    getchar();
    char enter;
    scanf("%c",&enter);
    for (int i = 0; i < 14; i++)//전체 카드 돌리는 함수
    {
        int number = 1;//카드에 들어가는지 확인 할 숫자
        int remainder_number[14] = { 0 };//숫자의 나머지로 나온 수들(이진수) 배열에 저장
        int number_box = 0;;//수의 나머지로 이진수를 구하는 과정에서 바뀌는 수(원본numner 값이 변하지 않기 위해)
        for (int j = 0; j < biggest_Number-1; j++)//카드내의 최대값까지 수를 확인하면 돌리는 for문
        {
            
            number_box = number;
            
            for (int c = 0; c < numbers_of_card; c++)//수가 카드에 들어가는 숫자인지 확인하는 2진수로 배열에 저장하는 함수
            {
                    if (number_box < 2)//number_box가 2보다 작으면 수를 더 건들면 안됌
                    {
                        remainder_number[c] = number_box % 2;
                        break;
                    }
                    remainder_number[c] = number_box % 2;//나머지 값을 배열에 저장
                    number_box = number_box / 2;//몫을 number 박스에 저장, 다음 나머지를 구하기 위한 값
                    
                
            }//배열에 2진수 순서로 저장
            if (remainder_number[i] == 1)//이진수로 바꾸고 자리를 확인해서 1이라면
            {
                array[i][j] =number;//그 자리에 해당하는 카드에 number값을 대입
            }
            
            number++;//다음값을 확인하기 위해 number를 증가


        }
    }


 int answers[14]={0};
    for (int i = 0; i < numbers_of_card; i++)
    {
        printf("|");
        
        for(int x=0;x<numbers_of_card*5+(numbers_of_card-2);x++)
        {
            printf("-");
            if(x==(numbers_of_card*5+(numbers_of_card-2))/2)
            {
                printf("%c",i+65);

            }
        }
        
             
        printf("|");
        printf("\n");
        printf("|");
        int num=0;
        for (int j = 0; j < 16384; j++)
        {
            if(num==numbers_of_card)
            {
                printf("|\n|");
                num=0;
            }
            if (array[i][j] != 0)
            {
                if(num==numbers_of_card-1)
                {
                    printf("%5d", array[i][j]);
                num++;
                }
                else
                {
                    printf("%5d ", array[i][j]);
                num++;
                }
                
                if(array[i][j]==biggest_Number-1)
                {
                    for(int x=0;x<numbers_of_card-num;x++)
                    {
                        printf("%6s","");
                    }
                    if(num%4==0)
                    {
                        printf("|");
                    }
                    else
                    printf("\b|");
                    break;
                }
            }
            
           
        }
        printf("\n");
        printf("|");
        
        for(int x=0;x<numbers_of_card*5+(numbers_of_card-1);x++)
        {
            printf("-");
        }
        printf("|");
        printf("\n");


        int answer;
       
        printf("\n이 중에 생각하신 숫자가 있습니까?있으면 1 없으면 0:");
        scanf("%d",&answer);
        if(answer==1)
        {
            answers[i]=1;
        }
        else
        {
            answers[i]=0;
        }
        printf("\n");
    }
    
    int result=0;
    for(int i=0;i<numbers_of_card;i++)
    {
        result+=answers[i]*pow(2,i);
    }

    printf("%d 입니다.",result);

}