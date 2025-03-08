from manim import *
from MF_Tools import *
 
class dem0(Scene):
    def construct(self):
        int = MathTex(r"\int  x^{2}e^{x} \, dx").scale(1.5)
        intf = MathTex(r"\int  x^{2}e^{x} \, dx = u\,v - \int v\, du").scale(1.5).to_edge(UP)
        intr = MathTex(r"\int  x^{2}e^{x} \, dx = x^{2}e^{x} -\int 2xe^{x} \, dx").scale(1.5).to_edge(UP)
        
 
        Derivo = MathTex(r"\text{Derivo}").scale(1.33)
        Derivo1 = MathTex(r"u = x^2").scale(1.5)
        Derivo2 = MathTex(r"\frac{du}{dx}=2x").scale(1.5)
 
        Derivo1[0][0:1].set_color(BLUE)
 
        Derivado = VGroup(Derivo,Derivo1,Derivo2).arrange(DOWN, buff=1)
 
        Integro = MathTex(r"\text{Integro}").scale(1.33)
        Integro1 = MathTex(r"dv = e^{x}\, dx").scale(1.5)
 
        Integrado = VGroup(Integro, Integro1).arrange(DOWN, buff=1)
 
        Formula = VGroup(Derivado, Integrado).arrange(RIGHT, buff=2).to_edge(DOWN)
 
        Derivo3 = MathTex(r"du=2x\,dx").scale(1.5).move_to(2*DOWN + 2.5*LEFT)
        Derivo3[0][0:2].set_color(BLUE)
 
        
        Integro2 = MathTex(r"\int dv = \int e^{x}\, dx").scale(1.5).move_to(2*DOWN + 2.5*RIGHT)
        Integro3 = MathTex(r"v = e^{x}").scale(1.5).move_to(Integro2)
        Integro3[0][0:1].set_color(ORANGE)
        
        int0 = MathTex(r"\int  x^{2}e^{x} \, dx = x^{2}e^{x} -2\int xe^{x} \, dx").scale(1.5)
        int1 = MathTex(r"\int  x^{2}e^{x} \, dx = x^{2}e^{x}-2(x-1) \,e^{x} + C").scale(1.5)
        int2 = MathTex(r"\int  x^{2}e^{x} \, dx = \left[x^{2}-2(x-1) \right] e^{x} + C").scale(1.5)
        int3 = MathTex(r"\int  x^{2}e^{x} \, dx = \left[x^{2}-2x+2 \right] e^{x} + C").scale(1.5)
 
        intf[0][8:9].set_color(BLUE)
        intf[0][9:10].set_color(ORANGE)
        intf[0][12:13].set_color(ORANGE)
        intf[0][13:15].set_color(BLUE)
        
        intr[0][8:10].set_color(BLUE)
        intr[0][10:12].set_color(ORANGE)
        intr[0][14:16].set_color(BLUE)
        intr[0][16:18].set_color(ORANGE)
        intr[0][18:20].set_color(BLUE)
 
        XD = ImageMobject(r"assets\img\otario")
        XD.scale(1.5)
        
        self.add(int)
        self.wait()
        self.play(TransformByGlyphMap(int, intf,
            ([0,1,2,3,4,5,6],[0,1,2,3,4,5,6], {"run_time":0.75}),
            (Write,[7], {"run_time": 2}),
            (Write,[8,9,10,11,12,13,14], {"run_time": 2, "delay":0.5})
                                        ))
        self.wait()
 
        self.play(Write(Derivo),Write(Integro))
        
        self.play(TransformByGlyphMap(intf, Derivo1,
            ([0,1,3,4,5,6,7,8,9,10,11,12,13,14],RemoveTextLetterByLetter),
            ([1,2],[2,3], {"delay":0.8}),
            (Write,[0,1]),
            from_copy=True,
            remove_individually=True
                                    ))
        
 
        self.play(TransformByGlyphMap(intf, Integro1,
            ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],RemoveTextLetterByLetter),
            ([3,4,5,6],[3,4,5,6], {"delay":0.8}),
            (Write,[0,1,2]),
            from_copy=True,
            remove_individually=True
                                    ))
        
    
        self.play(TransformByGlyphMap(Derivo1, Derivo2,
            ([0,1,2,3],Add),
            (Write,[0,2,3,4,5]),
            ([0],[1],{"delay":0.6}),
            ([2,3],[7,6],{"delay":0.6}),
            introduce_individually=True
                                    ))
        
        self.play(TransformByGlyphMap(Derivo2, Derivo3,
            ([2],FadeOut),
            ([0,1,5,6,7],[0,1,2,3,4]),
            ([3,4],[5,6], {"Path_arc": PI}),
            introduce_individually=True
                                    ))
        
        self.play(TransformByGlyphMap(Integro1, Integro2,
            (FadeIn,[0,4]),
            ([0,1,2,3,4,5,6],[1,2,3,5,6,7,8]),
            introduce_individually=True
                                    ))
 
        self.play(TransformByGlyphMap(Integro2, Integro3,
            ([0,1,4,7,8],FadeOut),
            ([2,3,5,6],[0,1,2,3]),
                                    ))
 
        self.play(TransformByGlyphMap(intf, intr,
            ([0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]),
            ([8],[8,9]),
            ([9],[10,11]),
            ([10],[12]),
            ([11],[13]),
            ([12],[16,17]),
            ([13,14],[14,15,18,19])
                                        ))
        self.wait() 
        self.play(FadeOut(Derivo,Integro,Derivo1,Derivo3,Integro3))
 
        self.play(TransformByGlyphMap(intr, int0,
            ([0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,3,4,5,6,7,8,9,10,11,12]),
            ([14],[13]),
            ([14],[13]),
            ([15,16,17,18,19],[15,16,17,18,19]),
                                        ))
        self.wait(1.5) 
        self.play(TransformByGlyphMap(int0, int1,
            ([0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13]),                          
            ([16,17],[19,20]),                          
            ([15],[15]),
            ([],[14,16,17,18]),                          
            ([14,18,19],[]),                          
            ([],[21,22])                          
                                      ))
        self.wait()
        self.play(TransformByGlyphMap(int1, int2,
            ([0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]),
            ([8,9],[9,10]),
            ([10,11],[19,20], {"path_arc":2/3*PI}),
            ([19,20],[], {"run_time": 1.2}),
            ([12,13,14,15,16,17,18],[11,12,13,14,15,16,17]),
            ([],[8,18]),
            ([21,22],[21,22])
                                      ))
        self.wait()
        self.play(TransformByGlyphMap(int2, int3,
            ([0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]),
            ([8,18],[8,16]),
            ([9,10,11],[9,10,11]),                          
            ([12],[12,15]),
            ([14],[13]),
            ([11],[14]),
            ([15],[]),
            ([13,16,17],[]),                                                    
            ([19,20,21,22],[17,18,19,20])                                                    
                                      ))
        self.wait(2)                              
        self.play(FadeIn(XD))
        self.wait()
