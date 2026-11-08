#include <iostream>
using namespace std;

// Node Structure
struct Node
{
    int data;
    Node *next;
};

Node *head = NULL;

// Function to Create Linked List
void createList(int value)
{
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL)
    {
        head = newNode;
    }
    else
    {
        Node *temp = head;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Function to Delete a Node
void deleteNode(int value)
{
    if (head == NULL)
    {
        cout << "List is empty." << endl;
        return;
    }

    Node *temp = head;
    Node *prev = NULL;

    // If first node contains the value
    if (temp != NULL && temp->data == value)
    {
        head = temp->next;
        delete temp;
        cout << "Element deleted successfully." << endl;
        return;
    }

    // Search for the node
    while (temp != NULL && temp->data != value)
    {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL)
    {
        cout << "Element not found." << endl;
        return;
    }

    prev->next = temp->next;
    delete temp;

    cout << "Element deleted successfully." << endl;
}

// Function to Display Linked List
void display()
{
    Node *temp = head;

    if (temp == NULL)
    {
        cout << "Linked List is empty." << endl;
        return;
    }

    cout << "Linked List: ";

    while (temp != NULL)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }

    cout << "NULL" << endl;
}

// Main Function
int main()
{
    int n, value, delValue;

    cout << "Enter the number of nodes: ";
    cin >> n;

    cout << "Enter the elements:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> value;
        createList(value);
    }

    cout << "\nOriginal ";
    display();

    cout << "\nEnter the element to delete: ";
    cin >> delValue;

    deleteNode(delValue);

    cout << "\nAfter Deletion ";
    display();

    return 0;
}