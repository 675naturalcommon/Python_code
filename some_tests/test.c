#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>
#include<windows.h>

//int main()
//{
//	char arr1[] = "Hello,the princess of ����!";
//	char arr2[] = "                           ";
//
//	int left = 0;
//	int right = strlen(arr1) - 1;//arr���ȴ�0��ʼ,������Ҫ��1
//
//	while (left <= right)
//	{
//		arr2[left] = arr1[left];
//		arr2[right] = arr1[right];
//		Sleep(1000);//����1000����
//		system("cls");//��տ���̨��Ļ��Ϣ
//		printf("%s\n", arr2);
//		left++;
//		right--;
//	}
//	return 0;
//}

int main()
{
	char arr1[] = "堃堃,actually,I want to say you are sb!";
	char arr2[] = "                                       ";

	int left = 0;
	int right = strlen(arr1) - 1;

	while (left <= right)
	{
		arr2[left] = arr1[left];
		arr2[right] = arr1[right];
		Sleep(1000);
		system("cls");
		printf("%s\n", arr2);
		left++;
		right--;
	}
	return 0;
}