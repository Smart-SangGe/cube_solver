class cube():
    """
    定义一个三阶魔方类
    """
    
    def __init__(self,cubestring:str) -> None:
        """
        定义魔方初始状态和解决状态

        Args:
            cube_strings (str): 传入cube_strings来表示魔方的状态
            
                 |************|
                 |*U1**U2**U3*|
                 |************|
                 |*U4**U5**U6*|
                 |************|
                 |*U7**U8**U9*|
                 |************|
     ************|************|************|************
     *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
     ************|************|************|************
     *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
     ************|************|************|************
     *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
     ************|************|************|************
                 |************|
                 |*D1**D2**D3*|
                 |************|
                 |*D4**D5**D6*|
                 |************|
                 |*D7**D8**D9*|
                 |************|
        
        输入时按照 U R F D L B 的顺序输入
        不区分颜色,以中心块的颜色决定。例如F5为红色,则所有红色在输入时输入F
        """
        self.cubestring = cubestring
        self.check_state(self.cubestring)
        self.solved_cubestring = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        
    def _check_state(self)->ValueError:
        """
        检查初始状态

        Returns:
            ValueError: 若输入不存在的状态,则报错退出
        """
        
        
        corner1 =  
        corner2 = 
        corner3 = 
        corner4 = 
        corner5 = 
        corner6 = 
        corner7 = 
        corner8 = 
        
        
        
    def solve(self,cubestring:str):