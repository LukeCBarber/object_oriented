
class Smartphone:

    
    #contructor
    def __init__(self, capacity, name):
        self.appspace = 0
        self.capacity = int(capacity)
        self.name = name
        self.apps = {}
        print("Smartphone created!")
        
    def add_app (self, appname, appsize):
        self.space = self.capacity - self.appspace
        self.appname = appname
        self.appsize = int(appsize)
        if self.appname not in self.apps:
            avaspace = self.space - self.appsize
            if avaspace > 0:
                self.apps[self.appname] = self.appsize
                self.appspace += self.appsize
                print("App successfully added")
            else:
                print("Error: storage full")
        else:
            print("Error: App already downloaded")
        
    def remove_app (self, appname):
        self.appname = appname
        if self.appname in self.apps:
            self.appspace -= self.apps.get(appname)
            del self.apps[self.appname]
            print('App removed:',appname)
        else:
            print("Error: app not found")
            return False

    def has_app(self, appname):
        self.appname = appname
        if self.appname in self.apps:
            return True
        else:
            return False

    def get_available_space(self):
        return self.capacity
    
    def report(self):
        self.space = self.capacity - self.appspace
        print('Name:',self.name)
        print('Capacity:', self.appspace,"out of", self.capacity,"GB")
        print('Available space:', self.space,"GB")
        print('Apps installed', len(self.apps))
        for item in self.apps:
            print('-',item,'is using',self.apps.get(item),'GB')



def main():
    capacity = int(input('Size of your new smartphone (32, 64, or 128 GB):'))
    name = input('Smartphone name:')
    smartphone = Smartphone(capacity,name)
    smartphone.report()
    print()
    end = False
    while end == False:
        decision = input('(r)eport, (a)dd, r(e)move app or (q)uit:')
        if decision == 'r':
            smartphone.report()
            print()
        elif decision == 'a':
            appname = input('App name to add:')
            appsize = input('App size in GB:')
            if appsize.isnumeric() == False:
                print('Invalid app size')
                print()
            else:
                smartphone.add_app(appname, appsize)
                print()
        elif decision == 'e':
            appname = input('App name to remove:')
            smartphone.remove_app(appname)
            print()
        elif decision == 'q':
            print('Goodbye!')
            end = True            
main()
    
    


        

        
    
    
