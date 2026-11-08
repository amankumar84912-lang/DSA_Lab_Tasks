#include <iostream>
using namespace std;

void merge(int a[], int l, int m, int r)
{
    int b[100], i = l, j = m + 1, k = l;

    while (i <= m && j <= r)
        b[k++] = (a[i] < a[j]) ? a[i++] : a[j++];

    while (i <= m) b[k++] = a[i++];
    while (j <= r) b[k++] = a[j++];

    for (i = l; i <= r; i++)
        a[i] = b[i];
}

void sort(int a[], int l, int r)
{
    if (l < r)
    {
        int m = (l + r) / 2;
        sort(a, l, m);
        sort(a, m + 1, r);
        merge(a, l, m, r);
    }
}

int main()
{
    int n, a[100];

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> a[i];

    sort(a, 0, n - 1);

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}