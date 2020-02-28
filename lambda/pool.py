"""
The NumberPool is a lowest available number checkout system. When a new instance is created, it logically contains all counting numbers 1-Long.MAX_VALUE. This means a call to checkout immediately after instantiation will return 1. The next checkout will return 2, and so on. When a number is checked back into the pool, it becomes available again and will be checked out when it becomes the lowest value in the pool.

Implement the following using test driven development.

 interface NumberPool {
   public long checkout();
   public void checkin(long i);
 }

Some reasonable tests include

testSimpleCheckout

 for (int i = 1; i < 10; i++) {
   np.checkout() == i;
 }

testPutNumberBack

 np.checkout() == 1; 
 np.checkout() == 2; 
 np.checkin(1);
 np.checkout() == 1;

testPutSeveralNumbersBack

 for (int i = 1; i < 10; i++) {
   np.checkout() == i;
 } 
 np.checkin(3);
 np.checkin(6);
 np.checkout() == 3;
 np.checkout() == 6; 
 np.checkout() == 10;


"""

class NumberPool:
    def __init__(self):
        self.counter = 1
        self.pool = set()

    def checkout(self):
        "Keep set of all loaned out numbers."

        # Check and see if there is a used number to lend out (don't use new)
        for i in range(1, self.counter + 1):
            if i not in self.pool:
                self.pool.add(i)
                return i

        # Return a brand new number
        self.counter += 1
        self.pool.add(self.counter)
        return self.counter

    def checkin(self, num):
        "Removed number from loaned out list"
        assert num in self.pool
        self.pool.remove(num)

    def checkout(self):
        "Keep set of all returned numbers"
        for i in range(1, self.counter + 1):
            if i in self.pool:
                self.pool.remove(i)
                return i
        result = self.counter
        self.counter += 1
        return result

    def checkin(self, num):
        "Add number to returned list"
        assert num not in self.pool
        self.pool.add(num)

np = NumberPool()
print(np.checkout())
print(np.checkout())
print(np.checkout())
np.checkin(1)
print(np.checkout())


tests = []
def unittest(func):
    tests.append(func)
    return func

@unittest
def test_checkout():
    np = NumberPool()
    for i in range(1, 10):
        assert np.checkout() == i
    
@unittest
def test_checkin():
    np = NumberPool()
    assert np.checkout() == 1
    assert np.checkout() == 2
    np.checkin(1)
    assert np.checkout() == 1

@unittest
def test_put_several_numbers_back():
    np = NumberPool()
    for i in range(1, 10):
        np.checkout()
    np.checkin(3)
    np.checkin(6)
    assert np.checkout() == 3
    assert np.checkout() == 6
    assert np.checkout() == 10



if __name__ == '__main__':
    for test in tests:
        failed = False
        try:
            test()
        except AssertionError:
            failed = True
        finally:
            print('Test:', test.__name__, 'failed.' if failed else 'succeeded!')
