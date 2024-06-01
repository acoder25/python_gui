#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct node{
	int data;
	struct node*left;
	struct node*right;
};
struct queuenode{
	struct node*data;
	struct queuenode*next;
};
struct queuenode*front=0,*rear=0;
void enqueue(struct node*newnode){
	struct queuenode*new1;
	new1=(struct queuenode*)malloc(sizeof(struct queuenode));
	new1->data=newnode;
	new1->next=0;
	if(rear==0){
		front=new1;
	}
	else{
		rear->next=new1;
	}
	rear=new1;
	
	
}
int cl=0;
int countln(struct node*root){
	if(root==NULL)
	return 0;
	if(root->left==NULL && root->right==NULL){
		cl++;
	}
	countln(root->left);
	countln(root->right);
	return cl;
	
}
struct node*dequeue(){
	if(front==0){
		return 0;
	}
	if(rear==front)
	rear=0;
	struct queuenode* temp = front;
    struct node* treenode = temp->data;
	front=front->next;
	
	free(temp);
	return treenode;
	
}
struct node*create(int x){
	struct node*newnode;
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->left=0;
	newnode->right=0;
	if(x==-1){
		return 0;
	}
	newnode->data=x;
	int y,z;
	printf("enter left child of %d\n",x);
	scanf("%d",&y);
	newnode->left=create(y);
	printf("enter right child of %d\n",x);
	scanf("%d",&z);
	newnode->right=create(z);
	return newnode;
	
	
}
void display(struct node*root){
	if(root==0)
	return;
	display(root->left);
	printf("%d ",root->data);
	display(root->right);
	printf("\n");
}
int n=7;
int arr[7];
void level(struct node*root){int k=0;
	if (root == 0) {
        return;
    }
    enqueue(root);
    while (front != NULL) {
    struct node* current = dequeue();
    printf("%d\n", current->data);
    arr[k]=current->data;
    k++;

    if (current->left != NULL) {
      enqueue(current->left);
      printf("Enqueued Left Child: %d\n", current->left->data);
	  
    }
    if (current->right != NULL) {
      enqueue(current->right);
      printf("Enqueued Right Child: %d\n", current->right->data);
    }

  }
}
int max=0;
int findmax(struct node*root){
	if(root==NULL)
	return -1;
	else{
		if(max<root->data){
			max=root->data;
		}
		findmax(root->left);
		findmax(root->right);
	}
	return max;
	
}
int min=10000;
int findmin(struct node*root){
	if(root==NULL)
	return -1;
	else{
		if(min>root->data){
			min=root->data;
		}
		findmin(root->left);
		findmin(root->right);
	}
	return min;
	
}
int c=0;
int count(struct node*root){
	if(root==NULL){
		return 0;
	}
	c++;
	count(root->left);
	count(root->right);
	return c;
}
struct node*search(struct node*root,int y){
	if(root==NULL){
		return 0;
	}
	if(root->data==y){
		printf("found\n");
		return root;
	}
	struct node*leftsrch=search(root->left,y);
	struct node*rightsrch=search(root->right,y);
	
	if(leftsrch!=NULL){
		return leftsrch;
	}
	else if(rightsrch!=NULL){
		return rightsrch;
	}
	else{
		return 0;
	}	
}
int b[8];
void insertheap(int arr[7],int n,int value){
	int temp,i;
	for(i=0;i<n;i++){
		b[i]=arr[i];
	}
	b[n]=value;
	i=n;
	int parent;
	while(i>0){
		parent=floor((i-1)/2);
		if(b[parent]<b[i]){
			temp=b[parent];
			b[parent]=b[i];
			b[i]=temp;
			i=parent;
			
		}
		else{
			return;
		}
		
	}
}
int main(){
	
	struct node*root;
	int x,j;
	
	printf("enter data\n");
	scanf("%d",&x);
	root=create(x);
//	printf("\n");
//	printf("%d\n",findmax(root));
//	printf("%d\n",findmin(root));
//	printf("%d\n",count(root));
//	printf("element is found at:%d",search(root,4));
//	printf("no of leaf nodes:%d",countln(root));
    level(root);
    insertheap(arr,n,50);
    for(j=0;j<n+1;j++){
    	printf("%d",b[j]);
	}
	
}
