from color import colors

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
        self.cubestring.replace(" ", "").upper()
        self._check_state()
        self.solved_cubestring = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        
    def _check_state(self)->ValueError:
        """
        检查初始状态是否为一个存在的魔方状态

        Returns:
            ValueError: 若输入不存在的状态,则报错退出
            存在以下可能的错误
            1: 缺少某一些颜色,多出某一些颜色
            2: 并非所有12个边恰好存在一次
            3: 存在边块需要被翻转
            4: 并非所有8个角块恰好存在一次
            5: 旋转错误:一个角块需要被旋转
            6: 奇偶错误:两个角块或两个边块必须被交换
        """
        
        count = [0] * 6
        try:
            for i in range(54):
                assert self.cubestring[i] in colors
                count[colors[self.cubestring[i]]] += 1
        except:
            raise ValueError("cube string存在输入错误")
        
        for i in range(6):
            if count[i] != 9:
                raise ValueError("缺少某一些颜色,多出某一些颜色")
            
        
        
    def solve(self)->int:
        return 0