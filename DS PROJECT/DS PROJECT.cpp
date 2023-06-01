#include<iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std; 


void searching();
void recommendation();
 int main(){ 
	system("cls");
	int inp;
	
	//dataset filtering
	 string input_filename = "biggerdatasetcorrect.txt";
    ifstream input_file(input_filename);

    if (!input_file.is_open()) {
        cerr << "Error: could not open input file " << input_filename << endl;
        return 1;
    }

    string line;
    while (getline(input_file, line)) {
        int tilde_count = 0;
        string filename;
        vector<string> substrings;
        stringstream ss(line);
        string token;
        while (getline(ss, token, '~')) {
            tilde_count++;
            if (tilde_count > 4) {
                substrings.push_back(token);
            }
            if (tilde_count == 5) {
                filename = token;
            }
        }

        for (const auto& substring : substrings) {
            ofstream output_file;
            output_file.open(substring, ios::app);
            if (!output_file.is_open()) {
                cerr << "Error: could not open output file " << substring << endl;
                continue;
            }
            output_file << line << "\n";
            output_file.close();
        }
    }

	 


    input_file.close();
    

	
	cout<<"1) Search a Movie"<<endl<<"2) Recommend Movies "<<endl<<"3) Exit"<<endl;
	cin>>inp;
	if(inp==1){
		searching();
	}
	else if(inp==2){
		recommendation();
	}
	else if(inp==3){
		return 0;
	}
	
}
//bst node
class TreeNode {
public:
    string data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(const string& value) : data(value), left(nullptr), right(nullptr) {}
};

//maxHeap node
class Node {
public:
    string movieName;
    float rating;

    Node(const string& name, float rating) : movieName(name), rating(rating) {}
};

class MaxHeap {
public:
    MaxHeap(int capacity) : capacity(capacity), size(0) {
        heap = new Node*[capacity];
    }

    ~MaxHeap() {
        delete[] heap;
    }

    void insert(const string& movieName, float rating) {
        if (size == capacity) {
            cout << "Heap is full. Cannot insert more elements." << endl;
            return;
        }

        Node* newNode = new Node(movieName, rating);
        heap[size] = newNode;
        siftUp(size);
        size++;
    }

    Node* extractMax() {
        if (size == 0) {
            return nullptr;
        }

        Node* maxNode = heap[0];
        heap[0] = heap[size - 1];
        size--;
        siftDown(0);
        return maxNode;
    }

private:
    Node** heap;
    int capacity;
    int size;

    void siftUp(int index) {
        int parentIndex = (index - 1) / 2;
        while (index > 0 && heap[index]->rating > heap[parentIndex]->rating) {
            swap(heap[index], heap[parentIndex]);
            index = parentIndex;
            parentIndex = (index - 1) / 2;
        }
    }

    void siftDown(int index) {
        int maxIndex = index;
        int leftChildIndex = 2 * index + 1;
        int rightChildIndex = 2 * index + 2;

        if (leftChildIndex < size && heap[leftChildIndex]->rating > heap[maxIndex]->rating) {
            maxIndex = leftChildIndex;
        }

        if (rightChildIndex < size && heap[rightChildIndex]->rating > heap[maxIndex]->rating) {
            maxIndex = rightChildIndex;
        }

        if (maxIndex != index) {
            swap(heap[index], heap[maxIndex]);
            siftDown(maxIndex);
        }
    }
};


void insertNode(TreeNode*& root, const string& value) {
    if (root == nullptr) {
        root = new TreeNode(value);
        return;
    }

    if (value < root->data) {
        insertNode(root->left, value);
    } else if (value > root->data) {
        insertNode(root->right, value);
    }
}

void traverseInOrder(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    traverseInOrder(root->left);
    cout << root->data << endl;
    traverseInOrder(root->right);
}

bool isSubstringMatch(const string& substring, const string& searchInput) {
    string substringLower;
    for (char ch : substring) {
        substringLower += tolower(ch);
    }


    string searchInputLower;
    for (char ch : searchInput) {
        searchInputLower += tolower(ch);
    }

    return (substringLower.find(searchInputLower) != string::npos);
}

void searchNode(TreeNode* root, const string& searchInput) {
    if (root == nullptr) {
        return;
    }

    searchNode(root->left, searchInput);

    if (isSubstringMatch(root->data, searchInput)) {
        cout <<"-"<< root->data << endl;
    }
    searchNode(root->right, searchInput);
			
}

bool isFloatGreaterThanOrEqualTo(const  string& substring, float value) {
    try {
        float floatValue =  stof(substring);
        return (floatValue >= value);
    } catch ( exception&) {
        return false;
    }
}

string convertToFileName(const string& userInput) {
    string lowercaseInput = userInput;
    for (char& ch : lowercaseInput) {
        ch = tolower(ch);
    }

    string fileName = lowercaseInput ;
    return fileName;
}

void searching(){
	SearchingMenu:
	char i;
	system("cls"); 
  while(1){
	cout<<endl<<endl;
	int x;	
	cout<<"Search by : "<<endl<<"1) Name"<<endl<<"2) Genre"<<endl<<"3) Top rated" <<endl<< "4) Go to main menu"<<endl;
	cin>>x;
	cout << endl;
	if(x==1){

			 ifstream inputFile("biggerdatasetcorrect.txt");
		    if (!inputFile.is_open()) {
		        cout << "Failed to open the file." << endl;
		    }
		
		    TreeNode* root = nullptr;
		
		    string line;
		    while (getline(inputFile, line)) {
		        int firstTilde = line.find('~');
		        int secondTilde = line.find('~', firstTilde + 1);
		        int thirdTilde = line.find('~', secondTilde + 1);
		
		        string extractedString = line.substr(secondTilde + 1, thirdTilde - secondTilde - 1);
		        insertNode(root, extractedString);
		    }
		
		    inputFile.close();
		    
			string searchInput;
			cout << endl;
		    cout << "Search : ";
		    cin >> searchInput;
		
			cout << endl;
		    cout << "Are you looking for : " << endl;
		    searchNode(root, searchInput);
		
    cout << "Do you wish to continue ?(y/n) :" << endl;
    cin>> i;
	if(i == 'n' ){
		main();
	}
	else if(i == 'y'){
		goto SearchingMenu;
	}
		}
	
	if(x==2){
		
		string userInput;
		string arr[] = {"action", "adventure", "animation", "children", "comedy", "crime", "documentary", "drama", "fantasy", "film-noir", "horror", "imax", "musical", "mystery", "romance", "sci-fi", "thriller", "war", "western" };
				
				for(int i=0; i<19; i++){
					cout << "-" << arr[i] <<endl;
				}
				
				
				
				cout<<"Enter name of genre: ";
				cin>>userInput;
				string fileName = convertToFileName(userInput);
				
				//fileName[0] -= 32;
				cout << fileName<<endl;
				
				 ifstream inputFile(fileName);
			    if (!inputFile.is_open()) {
			        cout << "Failed to open the file." <<  endl;
			    }
			
			     string line;
			    int i=1;
			    while (getline(inputFile, line)) {
			    	
			        int firstTilde = line.find('~');
			        int secondTilde = line.find('~', firstTilde + 1);
			        int thirdTilde = line.find('~', secondTilde + 1);
			
			        string extractedString = line.substr(secondTilde + 1, thirdTilde - secondTilde - 1);
			        cout <<i<< ") " << extractedString <<  endl;
			        i++;
			    }
			
			    inputFile.close();
	char c;
    cout << "Do you wish to continue ?(y/n) :" << endl;
    cin>> c;
	if(c == 'n' ){
		main();
	}
	else if(c == 'y'){
		goto SearchingMenu;
	}			    
			 
	}
	
	if(x==3){
	
		MaxHeap maxHeap(10000);
    
    ifstream inputFile("biggerdatasetcorrect.txt");
	    if (!inputFile.is_open()) {
	        cout << "Failed to open the file." <<  endl;
	    }
	
	    float threshold = 4.0f;
	
		
	    string line;
	    while (getline(inputFile, line)) {
	        int firstTilde = line.find('~');
	        int secondTilde = line.find('~', firstTilde + 1);
	        int thirdTilde = line.find('~', secondTilde + 1);
	        int fourthTilde = line.find('~', thirdTilde + 1);
	
	        string extractedString = line.substr(secondTilde + 1, thirdTilde - secondTilde - 1);
	        string floatValueString = line.substr(thirdTilde + 1, fourthTilde - thirdTilde - 1);
			if (isFloatGreaterThanOrEqualTo(floatValueString, threshold)) {
			
				float value = stof(floatValueString);
	        	maxHeap.insert(extractedString, value);
				
	        }
	    }
	        inputFile.close();

    cout << "Top-Rated Movies" << endl;
    cout << endl;
    Node* maxNode;
    while ((maxNode = maxHeap.extractMax()) != nullptr) {
        cout << "-" << maxNode->movieName << ", Rating: " << maxNode->rating << endl;
        delete maxNode;
    }
	    
	char r;
    cout << "Do you wish to continue ?(y/n) :" << endl;
    cin>> r;
	if(r == 'n' ){
		main();
	}
	else if(r == 'y'){
		goto SearchingMenu;
	}			    
			 
	}
	
	
	
	if(x == 4){
		main();
	}
	
	
		
  }
	}
	

//recommendation functions and classes start	
class user {
public:
    int ID;
    int Action=0,Adventure=0,Animation=0,Children=0,Comedy=0,Crime=0,Documentary=0,Drama=0,Fantasy=0,Filmnoir=0,Horror=0,IMAX=0,Musical=0,Romance=0,SciFi=0,Thriller=0,War=0,Western=0;
    string fav_genre1;
    string fav_genre2;
    user* next;
};

class user_linkedlist {
private:
    user* head;
    int Action=0,Adventure=0,Animation=0,Children=0,Comedy=0,Crime=0,Documentary=0,Drama=0,Fantasy=0,Filmnoir=0,Horror=0,IMAX=0,Musical=0,Romance=0,SciFi=0,Thriller=0,War=0,Western=0;

public:
    user_linkedlist() {
        head = nullptr;
    }

    // function to add a new user to the linked list
    void add_user(int id, string genre1, string genre2) {
        // check if user with same ID already exists
       

        user* new_user = new user;
        new_user->ID = id;
        new_user->fav_genre1 = genre1;
        new_user->fav_genre2 = genre2;
        new_user->next = nullptr;

        if (head == nullptr) {
            head = new_user;
        }
        else {
            user* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = new_user;
        }
    }

    // function to check if a user with the given ID already exists in the linked list
void contains_user(int id) {
    user* temp = head;
    while (temp != nullptr) {
        if (temp->ID == id) {
            cout << "Favourite genre of User " << temp->ID << " is " << temp->fav_genre1 << endl;
            cout << "These are the " << temp->fav_genre1 << " movies :" << endl;
            cout << endl;
            
            // open file with name from fav_genre1
            ifstream infile(temp->fav_genre1);
            string line;
            while (getline(infile, line)) {
                size_t first = line.find("~");
                if (first != string::npos) {
                    size_t second = line.find("~", first+1);
                    if (second != string::npos) {
                        size_t third = line.find("~", second+1);
                        if (third != string::npos) {
                            size_t fourth = line.find("~", third+1);
                            if (fourth != string::npos) {
                                cout <<"- "<< line.substr(second+1, third-second-1);
                                cout <<" Rating: "<< line.substr(third+1, fourth-third-1) << endl;
                            }
                        }
                    }
                }
            }
            infile.close();
            return ;
        }
        temp = temp->next;
    }
    return ;
}





    // function to print the IDs of all users in the linked list
 

    // function to read a file and add users to the linked list
void read_file(string filename) {
    ifstream infile(filename);
    string line;
    while (getline(infile, line)) {
        stringstream ss(line);
        string token;
        int field_num = 0;
        int ID = 0;
        string genres[] = {"Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Filmnoir", "Horror", "IMAX", "Musical", "Romance", "SciFi", "Thriller", "War", "Western"};

        string fav_genre1 = "";
        string fav_genre2 = "";
        int max_count = 0;
        string max_genre = "";
        int genre_count[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        while (getline(ss, token, '~')) {
            field_num++;
            if (field_num == 2) {
                ID = stoi(token);
            }
            else if (field_num == 3) {
                fav_genre1 = token;
            }
            else if (field_num == 4) {
                fav_genre2 = token;
            }
            else {
                for (int i = 0; i < 18; i++) {
                    if (token == genres[i]) {
                        genre_count[i]++;
                        break;
                    }
                }
            }
        }
        // Find the genre variable with the highest count
        for (int i = 0; i < 18; i++) {
            if (genre_count[i] > max_count) {
                max_count = genre_count[i];
                max_genre = genres[i];
            }
        }
        add_user(ID,max_genre,fav_genre2);
    }
}

    // destructor to free the memory allocated for the linked list
    ~user_linkedlist() {
        user* temp = head;
        while (temp != nullptr) {
            user* next = temp->next;
            delete temp;
            temp = next;
        }
    }
};


	void recommendation(){
		system("cls");
			char inp='y';
			while(inp=='y'){
				system("cls");
			int ID;
			cout<<"Please enter your ID:";
			cin>>ID;
			cout << endl;
		    user_linkedlist users;
		    users.read_file("biggerdatasetcorrect.txt");
		    users.contains_user(ID);
		    cout<<endl;
			cout<<"Do you want recommendations for some other user?(y/n)";
			cin>>inp;
			}
			main();
		 	return ;
		 	
	}

	




