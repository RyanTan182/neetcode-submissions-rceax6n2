class Solution:
    def reverseBits(self, n: int) -> int:
        final_int = 0
        for i in range(32):
            print("I range:", i)
            lsb_turned_msb = (n >> i) & 1
            print("Current LSB in n: ", lsb_turned_msb)
            final_int |= (lsb_turned_msb << (32 - i - 1))
        
        # self.print_all_bits(final_int)
        
        return final_int
    
    
        

        