from manim import *
import numpy as np

# Total render time: 2-3 hours
# There render time is depend how fast pc is
# render time per part is 30-50 minutes
# font used is new computer modern

## TIMELINE

class StarSelection(Scene): # similar AstroCat or Dogepro
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW):
            glow_group = VGroup(*[Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)]).move_to(vmobject)
            return glow_group
        star_o_base = Dot(radius=0.9,color="#5b7cff")        
        star_o_glow = create_glow(star_o_base,rad=3,col="#5b7cff")
        star_o = VGroup(star_o_base,star_o_glow)
        star_o.shift(LEFT*6)
        star_b_base = Dot(radius=0.81,color="#718fff")        
        star_b_glow = create_glow(star_b_base,rad=2.5,col="#718fff")
        star_b = VGroup(star_b_base,star_b_glow)
        star_b.shift(LEFT*3.5)
        star_a_base = Dot(radius=0.74,color="#9ab0ff")        
        star_a_glow = create_glow(star_a_base,rad=2.2,col="#9ab0ff")
        star_a = VGroup(star_a_base,star_a_glow)
        star_a.shift(LEFT*1.3)
        star_f_base = Dot(radius=0.64,color="#ebe7ff")        
        star_f_glow = create_glow(star_f_base,rad=1.8,col="#ebe7ff")
        star_f = VGroup(star_f_base,star_f_glow)
        star_f.shift(RIGHT*0.7)
        star_g_base = Dot(radius=0.53,color="#ffe8d7")        
        star_g_glow = create_glow(star_g_base,rad=1.5,col="#ffe8d7")
        star_g = VGroup(star_g_base,star_g_glow)
        star_g.shift(RIGHT*2.6)
        star_k_base = Dot(radius=0.44,color="#ffac6f")        
        star_k_glow = create_glow(star_k_base,rad=1.2,col="#ffac6f")
        star_k = VGroup(star_k_base,star_k_glow)
        star_k.shift(RIGHT*4.2)
        star_m_base = Dot(radius=0.32,color="#ffa448")        
        star_m_glow = create_glow(star_m_base,rad=0.9,col="#ffa448")
        star_m = VGroup(star_m_base,star_m_glow)
        star_m.shift(RIGHT*5.6)
        arrow_select = Triangle(fill_color=GREEN,stroke_width=0).rotate(PI).scale(0.6).next_to(star_o_base,UP)
        arrow_select.set_fill(GREEN,opacity=1)
        star_list = [star_o_base,star_b_base,star_a_base,star_f_base,star_g_base,star_k_base,star_m_base]
        star_spectral_type = [Text('O',font="NewComputerModern10"),
                              Text('B',font="NewComputerModern10"),
                              Text('A',font="NewComputerModern10"),
                              Text('F',font="NewComputerModern10"),
                              Text('G',font="NewComputerModern10"),
                              Text('K',font="NewComputerModern10"),
                              Text('M',font="NewComputerModern10")]
        for i in range(len(star_spectral_type)):
            star_spectral_type[i].next_to(star_list[i],DOWN).scale(0.92**i)
            self.add(star_spectral_type[i])
        self.add(star_o,star_b,star_a,star_f,star_g,star_k,star_m)
        self.add(arrow_select)  
        self.wait(2)
        #self.add_sound("snd_squeak.wav")
        self.play(arrow_select.animate.next_to(star_b_base,UP),run_time=1/6,rate_func=linear)
        self.wait(0.3)
        #self.add_sound("snd_squeak.wav")
        self.play(arrow_select.animate.next_to(star_a_base,UP),run_time=1/6,rate_func=linear)
        self.wait(0.3)
        #self.add_sound("snd_squeak.wav")
        self.play(arrow_select.animate.next_to(star_f_base,UP),run_time=1/6,rate_func=linear)
        self.wait(0.5)
        arrow_select.set_fill(GRAY,opacity=1)
        self.wait(0.25)
        #self.add_sound("snd_squeak.wav")
        #self.add_sound("ohyes.mp3")
        self.remove(star_o,star_b,star_a,star_f,star_g,star_k,star_m,arrow_select)
        for i in range(len(star_spectral_type)):
            self.remove(star_spectral_type[i])
        loading_texture = [Arc(radius=0.5, start_angle=0, angle=PI/2,color= GRAY,stroke_width=5),Arc(radius=0.5, start_angle=PI/2, angle=PI/2,color= GRAY_E,stroke_width=5),Arc(radius=0.5, start_angle=PI, angle=PI/2,color= GRAY,stroke_width=5),Arc(radius=0.5, start_angle=3*PI/2, angle=PI/2,color= GRAY_E,stroke_width=5)]
        loading = VGroup(*[loading_texture[i] for i in range(len(loading_texture))]).to_corner(DR)
        loading_text = Text('Please wait',font="NewComputerModern10")
        loading.add_updater(lambda mob,dt: mob.rotate(-360*DEGREES*dt))
        self.add(loading,loading_text)
        self.wait(3)
        loading.clear_updaters()
        self.remove(loading,loading_text)
        self.add(star_f)
        star_f.move_to(ORIGIN)
        star_names = Text('Fertumi',font="NewComputerModern10").next_to(star_f_base,DOWN,buff=0.25)
        star_mass = Text('Mass:1.48 Sun',font="NewComputerModern10").next_to(star_names,DOWN)
        self.add(star_names,star_mass[:5])
        self.wait()
        self.add(star_mass[5:6])
        self.wait(0.2)
        self.add(star_mass[6:7])
        self.wait(0.2)
        self.add(star_mass[7:8])
        self.wait(0.2)
        self.add(star_mass[8:9])
        self.wait(0.2)
        self.add(star_mass[9:])
        self.wait()
        self.play(star_names.animate.scale(1.5).set_opacity(0),star_mass.animate.scale(1.5).set_opacity(0),run_time=2,rate_functions=linear)
        self.remove(star_names,star_mass,star_f)
        note = Text('This Made with ManimCE',font="NewComputerModern10")
        self.add(note)
        self.wait(3)

class TimelineMainSequence(ZoomedScene):
    def construct(self):
        # THE FUNCTION
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        def planet_hot_glow_1500c(vmobject, rad=1, col=ORANGE): # if planet is hot, it glows
            glow_group = VGroup(Annulus(
                inner_radius=0.95*rad*(1.01**(idx)),
                outer_radius=1.05*rad*(1.01**(idx)), 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        def hz(lum=1): # Habitable zone radius is AU and luminosity is Sun
            inter = Annulus(inner_radius=0.79*lum**0.5, outer_radius=0.93*lum**0.5,fill_color= YELLOW,fill_opacity=0.2,stroke_width=0) # inner habitable zone
            hab = Annulus(inner_radius=0.93*lum**0.5, outer_radius=1.45*lum**0.5,fill_color= GREEN,fill_opacity=0.2,stroke_width=0)   
            outer = Annulus(inner_radius=1.45*lum**0.5, outer_radius=1.63*lum**0.5,fill_color= BLUE_B,fill_opacity=0.2,stroke_width=0) # outer habitable zone
            zone = VGroup(inter,hab,outer)
            return zone    
        def planet(earth=1,col="#423f50"): # Earth radius to AU
            size = Dot(radius=earth*4.26354e-5,fill_color=col)
            return size
        def star(sun=1,col="#423f50"): # Sun radius to AU
            size = Dot(radius=sun*0.0046524726,fill_color=col)
            return size
        def orbit(w=1,h=1,col=RED): # Orbit of planet
            orb = Ellipse(width=w*2,height=h*2,stroke_width=h,color=col)
            return orb
        def decimal_value(x):
            number_place = int(max(-np.log10(x) + 3,0))
            return number_place
        def luminosity(): # luminosity is Sun
            time = t.get_value()
            if t.get_value() <= -2e7:
                return 59.86311
            elif -2e7 < t.get_value() <= 0:
                return 0.89 + np.exp(4.077-(time/1e6+20)) + np.exp(time/3e6+1.33)
            elif 0 < t.get_value() <= 2.8e9:
                return 4.67 + (1.48 ** 3.5)*1e-10*3.21*time
            elif 2.8e9 < t.get_value() <= 2.85e9:
                return 8.2146 + (time-2.8e9)*4.72e-8
            elif 2.85e9 < t.get_value() <= 2.93e9:
                return 10.5746 - (time-2.85e9)*4.4e-8
            elif 2.93e9 < t.get_value() <= 3.06e9:
                return 7.0546 * np.exp((time-2.93e9)/5e7)
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 94.98128 * np.exp((time-3.06e9)/6e6)
            elif 3.08e9 < t.get_value() <= 3.1e9:
                return 62.34 * np.exp((time-3.08e9)/1e9)
            elif 3.1e9 < t.get_value() <= 3.2e9:
                return 63.5993 * np.exp((time-3.1e9)/1e8)
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 172.8808 * np.exp((time-3.2e9)/1.7e6)
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 2510.35208 * np.exp((time-3.205e9)/2.865e5)
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 2510.35208 * 1.0914394 * np.exp((time-3.2051e9)/2.865e5)
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 2510.35208 * 1.0914394**2 * np.exp((time-3.2052e9)/2.865e5)
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 2510.35208 * 1.0914394**3 * np.exp((time-3.2053e9)/2.865e5)    
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 2510.35208 * 1.0914394**4 * np.exp((time-3.2054e9)/2.865e5)      
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 2510.35208 * 1.0914394**5 * np.exp((time-3.2055e9)/2.865e5)  
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 2510.35208 * 1.0914394**6 * np.exp((time-3.2056e9)/2.865e5)      
            elif 3.2057e9 < t.get_value() <= 3.20673e9:
                return 6016.1503 / np.exp((time-3.2057e9)/1e5)
            elif 3.20673e9 < t.get_value() <= 3.37e9:
                return 0.2023417 / np.exp(np.log10((time-3.20673e9)/1e5+0.1)+1)
            else:
                return 0.0029952 / np.exp(np.log((time-3.37e9)/1e8+1))                                                     
        def radius(): # radius is Sun
            time = t.get_value()
            if t.get_value() <= -2e7:
                return 15.749731
            elif -2e7 < t.get_value() <= 0:
                return 0.87 + np.exp(-17.3-(time/1e6)) + np.exp(time/1e7-0.6)
            elif 0 < t.get_value() <= 2.8e9:
                return 1.4188 * np.exp(time/5.4e9)
            elif 2.8e9 < t.get_value() <= 2.85e9:
                return 2.3829 * np.exp((time-2.8e9)/5e8)
            elif 2.85e9 < t.get_value() <= 2.93e9:
                return 2.633511 * np.exp((time-2.85e9)/3.35e8)
            elif 2.93e9 < t.get_value() <= 3.06e9:
                return 3.343853 * np.exp((time-2.93e9)/8.4e7)
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 15.71699 * np.exp((time-3.06e9)/1e7)
            elif 3.08e9 < t.get_value() <= 3.1e9:
                return 12.01 * np.exp((time-3.08e9)/1e9)
            elif 3.1e9 < t.get_value() <= 3.2e9:
                return 12.25 * np.exp((time-3.1e9)/1.85e8)
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 21.032449 * np.exp((time-3.2e9)/2.4e6)
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 140.652 * np.exp((time-3.205e9)/3e5)
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 140.652*1.07 * np.exp((time-3.2051e9)/3e5)
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 140.652*1.07**2 * np.exp((time-3.2052e9)/3e5)
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 140.652*1.07**3 * np.exp((time-3.2053e9)/3e5)
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 140.652*1.07**4 * np.exp((time-3.2054e9)/3e5)
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 140.652*1.07**5 * np.exp((time-3.2055e9)/3e5)
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 140.652*1.07**6 * np.exp((time-3.2056e9)/3e5)
            else:
                return 0.0131 + 294.58688 / np.exp((time-3.2057e9)/1.456e4)
        def temperature(): # temperature of star
            return 5778*np.power(luminosity()/radius()**2,1./4)
        def color(): # Temperature to RGB and code from https://tannerhelland.com/2012/09/18/convert-temperature-rgb-algorithm-code.html
            temp = temperature() / 100
            if temp >= 67:
                r = 329.698727446046 * (temp-60)**-0.133204759227737
                g = 288.122169528293 * (temp-60)**-0.0755148492418579
                b = 255
            # exceed 255 or smaller than 0 will cause error become rgb must range 0 to 255
                r = min(max(0, r), 255)
                g = min(max(0, g), 255)
                b = min(max(0, b), 255)        
            else:
                r = 255    
                g = 99.4708025861262 * np.log(temp) - 161.119568166068
                g = min(max(0, g), 255)
                if temp < 20:
                    b = 0
                elif  20 <= temp <= 67:
                    b = 138.517761556144 * np.log(temp-10) - 305.044792730681
                    b = min(max(0, b), 255)
            return int(r),int(g),int(b)        
        def mass(): # Mass loss when red giant phase
            time = t.get_value()
            if -2e7 <= t.get_value() <= 3.06e9:
                return 1.48
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 1.48 - ((time-3.06e9)/8.5e7)**2
            elif 3.08e9 < t.get_value() <= 3.2e9:
                return 1.42463668
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 1.42463668 - ((time-3.2e9)/1.54e7)**2
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 1.31922261 - ((time-3.205e9)/3.075e5)**2
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 1.21346545 - ((time-3.2051e9)/3.075e5)**2
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 1.1077083 - ((time-3.2052e9)/3.075e5)**2
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 1.00195114 - ((time-3.2053e9)/3.075e5)**2
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 0.896193989 - ((time-3.2054e9)/3.075e5)**2
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 0.790436834 - ((time-3.2055e9)/3.075e5)**2      
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 0.684679679 - ((time-3.2056e9)/3.5e5)**2
            else:
                return 0.578922524                                                     
        def disk(rad=1, col=RED_C):
            planetary = VGroup(Circle(radius=rad*1.1**idx,fill_opacity=0.01-idx/6000,fill_color=col,stroke_width=0) for idx in range(50))
            return planetary
        # zoom camera first
        self.camera.frame.scale(5) # Zoom 5x
        # BASE #        
        rotate_deg = ValueTracker(0) # this make orbit changing even when star become red giant does to planet orbit expanding while star lose mass
        t = ValueTracker(-30e6)
        place_num = 0

        # PLANETARY DISK #
        planetary_disk = disk(rad=20)

        ## PHASE ZOOM 5x ##
        lum_text = Text('Luminosity (Sun):',font="NewComputerModern10").move_to([-4.6*5,2.5*5,0]).scale(0.8*5)
        lum_num = always_redraw(lambda: DecimalNumber(luminosity(),num_decimal_places=decimal_value(luminosity())).next_to(lum_text,RIGHT,buff=4).scale(5))
        zone = always_redraw(lambda: hz(lum=luminosity()))
        time_text = Text('Million years:',font="NewComputerModern10").move_to([-5.1*5,3.2*5,0]).scale(0.8*5)
        time_million = always_redraw(lambda: DecimalNumber(t.get_value()/1e6,num_decimal_places=place_num).next_to(time_text,RIGHT,buff=4).scale(5))
        temperature_text = Text('Temperature (K):',font="NewComputerModern10").move_to([-4.7*5,1.8*5,0]).scale(0.8*5)
        temperature_num = always_redraw(lambda: DecimalNumber(temperature(),num_decimal_places=0).next_to(temperature_text,RIGHT,buff=4).scale(5))
        radius_text = Text('Radius (Sun):',font="NewComputerModern10").move_to([-5.1*5,1.1*5,0]).scale(0.8*5)
        radius_num = always_redraw(lambda: DecimalNumber(radius(),num_decimal_places=decimal_value(radius())).next_to(radius_text,buff=3).scale(5))
        mass_text = Text('Mass (Sun):',font="NewComputerModern10").move_to([-5.35*5,0.4*5,0]).scale(0.8*5)
        mass_num = always_redraw(lambda: DecimalNumber(mass(),num_decimal_places=3).next_to(mass_text,buff=3).scale(5))
        star_base = always_redraw(lambda: star(sun=radius(),col=ManimColor.from_rgb(color())))
        star_glow = always_redraw(lambda: create_glow(star_base,rad=10*0.0046524726*radius(),col=ManimColor.from_rgb(color())))
        ### END ###

        ## ORBIT ##
        Mate_orbit = always_redraw(lambda: orbit(w=0.448*(1.48/mass()),h=0.437*(1.48/mass()),col=GRAY_A).move_to([0.0113*(1.48/mass()),0,0]).rotate((rotate_deg.get_value()+60)*DEGREES,about_point=ORIGIN))
        Scipli_orbit = always_redraw(lambda: orbit(w=2.98*(1.48/mass()),h=2.905*(1.48/mass()),col=GOLD_B).move_to([0.07829*(1.48/mass()),0,0]).rotate((rotate_deg.get_value()+120)*DEGREES,about_point=ORIGIN))
        Enecune_orbit = always_redraw(lambda: orbit(w=14.3*(1.48/mass()),h=13.45*(1.48/mass()),col=YELLOW_A).move_to([0.807*(1.48/mass()),0,0]).rotate((rotate_deg.get_value()-50)*DEGREES,about_point=ORIGIN))
        ### END ###

        ## INFO ZOOM 5x ##
        sq_info = VGroup(Square(side_length=1.3*5,fill_opacity=1,stroke_width=DEFAULT_STROKE_WIDTH*5,fill_color=GRAY_E) for _ in range(4)).arrange(RIGHT,buff=0).move_to([-4.5*5,-3.3*5,0])
        star_base_info = always_redraw(lambda: Dot(radius=0.42*5,color=ManimColor.from_rgb(color())).move_to(sq_info[0]))
        star_glow_info = always_redraw(lambda: create_glow(star_base_info,rad=2.1*3,col=ManimColor.from_rgb(color())))
        star_info = VGroup(star_base_info,star_glow_info)
        Mate_base = Dot(radius=0.35*5,fill_color=ORANGE).move_to(sq_info[1])
        Mate_hot_glow = planet_hot_glow_1500c(Mate_base,rad=0.35*5).scale(1)
        Mate = VGroup(Mate_base,Mate_hot_glow)
        Scipli_base = Dot(radius=0.35*5,fill_color=ORANGE).move_to(sq_info[2])
        Scipli_hot_glow = planet_hot_glow_1500c(Scipli_base,rad=0.35*5).scale(1)
        Scipli = VGroup(Scipli_base,Scipli_hot_glow)
        Enecune_base = Dot(radius=0.35*5,fill_color=ORANGE).move_to(sq_info[3])
        Enecune_hot_glow = planet_hot_glow_1500c(Enecune_base,rad=0.35*5).scale(1)
        Enecune = VGroup(Enecune_base,Enecune_hot_glow)
        # INFO TEXT ZOOM 5x #
        star_info_text = Text("Fertumi",font="NewComputerModern10").next_to(sq_info[0],UP,buff=1).scale(2)
        Mate_info_text = Text("Mate",font="NewComputerModern10").next_to(sq_info[1],UP,buff=1).scale(2)
        Scipli_info_text = Text("Scipli",font="NewComputerModern10").next_to(sq_info[2],UP,buff=1).scale(2)
        Enecune_info_text = Text("Enecune",font="NewComputerModern10").next_to(sq_info[3],UP,buff=1).scale(2)
        
        ### END ###
        # PRE MAIN
        self.add(t,rotate_deg,planetary_disk)
        self.add(time_text,time_million)
        t.add_updater(lambda mob,dt: mob.increment_value(5e6*dt))
        self.play(FadeIn(star_base,star_glow,sq_info,star_info,star_info_text),run_time=2)
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-60*dt))
        self.add(zone)
        self.wait(1.2) #-14 My
        self.add(Scipli_orbit)
        self.add(Scipli,Scipli_info_text)
        self.wait(0.6) #-11 My
        self.add(Enecune_orbit)
        self.add(Enecune,Enecune_info_text)
        self.wait(0.6) #-8 My
        self.add(Mate_orbit)
        self.add(Mate,Mate_info_text)
        self.wait(1.6) #0 My
        self.add(Scipli_orbit,Enecune_orbit)
        self.add(mass_text,mass_num,lum_num,lum_text,temperature_text,temperature_num,radius_num,radius_text)
        begin_nuclear_fusion = Text("begin thermonuclear fusion in Fertumi core",font="NewComputerModern10").scale(3).next_to(sq_info[3],RIGHT,buff=1)
        self.add(begin_nuclear_fusion)
        self.wait(2) #10 My
        self.remove(planetary_disk)
        self.wait(1.2) #16 My
        Mate[0].set_color(BLUE_A),self.remove(Mate[1])
        self.wait(1.6) #24 My
        Enecune[0].set_color(YELLOW_A),self.remove(Enecune[1])
        self.wait(1) #29 My
        Scipli[0].set_color(GOLD_B),self.remove(Scipli[1])
        self.wait(1) #34 My
        self.remove(begin_nuclear_fusion)
        self.wait(9.2) #80 My
        
        ### REMOVE UPDATER AND MOBJECTS ###
        #self.remove(info_group,orbit_group,text_zoom_5x,star_and_zone)
        rotate_deg.clear_updaters()
        t.clear_updaters()
        self.wait(0.1)        
        self.remove(star_info_text,Mate_info_text,Scipli_info_text,Enecune_info_text,sq_info,Mate_base,Scipli_base,Enecune_base,star_info)
        self.remove(Mate_orbit,Scipli_orbit,Enecune_orbit)
        self.remove(lum_text,lum_num,time_text,time_million,temperature_text,temperature_num,radius_text,radius_num,mass_text,mass_num)
        self.remove(zone,star_base,star_glow)
        ### END ###

        ### ZOOM IN AND SHIFT ###
        self.camera.frame.scale(1/5) # Zoom 1x
        ### COMPARSION ###
        Fertumi_comparsion = Dot(radius=1.438,fill_color=ManimColor.from_rgb((238, 240, 255)))
        Fertumi_comparsion_glow = create_glow(Fertumi_comparsion,rad=1.438*3,col=ManimColor.from_rgb((238, 240, 255)))
        Fertumi = VGroup(Fertumi_comparsion,Fertumi_comparsion_glow).shift(RIGHT*3+UP*1.438)
        Sol_comparsion = Dot(radius=1,fill_color=ManimColor.from_rgb((255, 242, 230)))
        Sol_comparsion_glow = create_glow(Sol_comparsion,rad=1*3,col=ManimColor.from_rgb((255, 242, 230)))
        Sol = VGroup(Sol_comparsion,Sol_comparsion_glow).shift(LEFT*3+UP)
        self.camera.frame.shift(3*UP)
        Sol_text = Text("Sol",font="NewComputerModern10").next_to(Sol_comparsion,UP)
        Fertumi_text = Text("Fertumi",font="NewComputerModern10").next_to(Fertumi_comparsion,UP)
        self.add(Fertumi,Sol,Fertumi_text,Sol_text)        
        self.wait(5)

        ### ZOOM IN AND ZOOM OUT ###
        self.remove(Fertumi,Sol,Fertumi_text,Sol_text)
        self.add(Mate_orbit,Scipli_orbit,Enecune_orbit,star_base,star_glow)
        self.camera.frame.scale(1/50).move_to(ORIGIN) # Zoom 1/50x
        self.wait(2)
        self.play(self.camera.frame.animate.scale(250),run_time=4) # Zoom 5x
        self.wait()
        self.play(self.camera.frame.animate.scale(0.2),run_time=2.5) # Zoom 1x
        self.wait(0.3)
        self.play(FadeIn(zone),run_time=2)
        self.wait(3)

        ## PART 2 ##
        lum_text_x = Text('Luminosity (Sun):',font="NewComputerModern10").move_to([-4.6,2.5,0]).scale(0.8)
        lum_num_x = always_redraw(lambda: DecimalNumber(luminosity(),num_decimal_places=decimal_value(luminosity())).next_to(lum_text_x,RIGHT,buff=0.6))
        time_text_x = Text('Million years:',font="NewComputerModern10").move_to([-5.1,3.2,0]).scale(0.8)
        time_million_x = always_redraw(lambda: DecimalNumber(t.get_value()/1e6,num_decimal_places=place_num).next_to(time_text_x,RIGHT,buff=0.6))
        temperature_text_x = Text('Temperature (K):',font="NewComputerModern10").move_to([-4.7,1.8,0]).scale(0.8)
        temperature_num_x = always_redraw(lambda: DecimalNumber(temperature(),num_decimal_places=0).next_to(temperature_text_x,RIGHT,buff=0.6))
        radius_text_x = Text('Radius (Sun):',font="NewComputerModern10").move_to([-5.1,1.1,0]).scale(0.8)
        radius_num_x = always_redraw(lambda: DecimalNumber(radius(),num_decimal_places=decimal_value(radius())).next_to(radius_text_x,buff=0.6))
        mass_text_x = Text('Mass (Sun):',font="NewComputerModern10").move_to([-5.35,0.4,0]).scale(0.8)
        mass_num_x = always_redraw(lambda: DecimalNumber(mass(),num_decimal_places=3).next_to(mass_text_x,buff=0.5))
        ## INFO ZOOM 1x ##
        sq_info_x = VGroup(Square(side_length=1.3,fill_opacity=1,fill_color=GRAY_E) for _ in range(4)).arrange(RIGHT,buff=0).move_to([-4.5,-3.3,0])
        star_base_info_x = always_redraw(lambda: Dot(radius=0.42,color=ManimColor.from_rgb(color())).move_to(sq_info_x[0]))
        star_glow_info_x = always_redraw(lambda: create_glow(star_base_info_x,rad=0.42*3,col=ManimColor.from_rgb(color())))
        star_info_x = VGroup(star_base_info_x,star_glow_info_x)
        Mate_base_x = Dot(radius=0.35,fill_color=BLUE_A).move_to(sq_info_x[1])
        Scipli_base_x = Dot(radius=0.35,fill_color=GOLD_B).move_to(sq_info_x[2])
        Enecune_base_x = Dot(radius=0.35,fill_color=YELLOW_A).move_to(sq_info_x[3])
        # INFO TEXT ZOOM 1x #
        star_info_text_x = Text("Fertumi",font="NewComputerModern10").next_to(sq_info_x[0],UP,buff=0.1).scale(0.4)
        Mate_info_text_x = Text("Mate",font="NewComputerModern10").next_to(sq_info_x[1],UP,buff=0.1).scale(0.4)
        Scipli_info_text_x = Text("Scipli",font="NewComputerModern10").next_to(sq_info_x[2],UP,buff=0.1).scale(0.4)
        Enecune_info_text_x = Text("Enecune",font="NewComputerModern10").next_to(sq_info_x[3],UP,buff=0.1).scale(0.4)
        self.add(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.add(sq_info_x,star_info_x,Mate_base_x,Scipli_base_x,Enecune_base_x)
        self.add(star_info_text_x,Mate_info_text_x,Scipli_info_text_x,Enecune_info_text_x)
        t.add_updater(lambda mob,dt: mob.increment_value(40e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-300*dt))
        self.wait(48.5) # 2020 My

        # CLEAR UPDATER
        rotate_deg.clear_updaters()
        t.clear_updaters()
        self.wait(0.1)        
        self.remove(star_info_text_x,Mate_info_text_x,Scipli_info_text_x,Enecune_info_text_x,sq_info_x,Mate_base_x,Scipli_base_x,Enecune_base_x,star_info_x)
        self.remove(Mate_orbit,Scipli_orbit,Enecune_orbit)
        self.remove(lum_text_x,lum_num_x,time_text_x,time_million_x,temperature_text_x,temperature_num_x,radius_text_x,radius_num_x,mass_text_x,mass_num_x)
        self.remove(zone,star_base,star_glow)
        
        # WIKI TIME
        self.camera.frame.scale(10).shift(30*UP) # zoom 10x out
        Fertumi_Base_Wiki_Comparsion = Dot(radius=30.121,color=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_Glow_Wiki_Comparsion = create_glow(Fertumi_Base_Wiki_Comparsion,rad=30.121*2,col=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_Wiki_Comparsion = VGroup(Fertumi_Base_Wiki_Comparsion,Fertumi_Glow_Wiki_Comparsion).move_to([-20,0,0]).shift(UP*30.121)
        Mate_Wiki_Comparsion = Dot(radius=1,color=BLUE_A).move_to([20,0,0]).shift(UP)
        Scipli_Wiki_Comparsion = Dot(radius=1.603,color=GOLD_B).move_to([25,0,0]).shift(UP*1.603)
        Enecune_Wiki_Comparsion = Dot(radius=1.468,color=YELLOW_A).move_to([30,0,0]).shift(UP*1.468)
        Fertumi_Wiki_Name = Text("Fertumi",font="NewComputerModern10").scale(10).next_to(Fertumi_Base_Wiki_Comparsion,UP,buff=2)
        Mate_Wiki_Name = Text("Mate",font="NewComputerModern10").next_to(Mate_Wiki_Comparsion,UP,buff=0.4)
        Scipli_Wiki_Name = Text("Scipli",font="NewComputerModern10").next_to(Scipli_Wiki_Comparsion,UP,buff=0.4)
        Enecune_Wiki_Name = Text("Enecune",font="NewComputerModern10").next_to(Enecune_Wiki_Comparsion,UP,buff=0.4)
        self.add(Fertumi_Wiki_Comparsion,Mate_Wiki_Comparsion,Scipli_Wiki_Comparsion,Enecune_Wiki_Comparsion,Fertumi_Wiki_Name)
        self.wait()
        self.play(self.camera.frame.animate.scale(1/5).move_to([25,6,0])) # zoom 2x out
        self.play(FadeOut(Fertumi_Wiki_Comparsion,Fertumi_Wiki_Name),FadeIn(Mate_Wiki_Name,Scipli_Wiki_Name,Enecune_Wiki_Name))
        self.play(self.camera.frame.animate.scale(1/4).move_to([18,1.5,0]),FadeOut(Mate_Wiki_Name,Scipli_Wiki_Name,Enecune_Wiki_Name)) # zoom 0.5x out
        self.wait(0.5)
        Mate_Wiki = Text("Mate\nHot sub-jupiter\nSemi-Major Axis: 0.437 AU (65.375 M km)\nOrbital Period: 86.724 days\nEccentricity:0.026\nMass: 0.109 jupiter (34.643 earth)\nRadius: 0.6658 jupiter (7.463 earth or 47,544 km)\nTemperature: 344.27°C (617.42 K)\nStellar flux: 37.859x as earth",font="NewComputerModern10").move_to([16.4,1.5,0]).scale(0.25)
        Scipli_Wiki = Text("Scipli\nCool super-jupiter\nSemi-Major Axis: 2.905 AU (434.588 M km)\nOrbital Period: 4.07 years (1,486.41 days)\nEccentricity:0.027\nMass: 2.49 jupiter (788.21 earth)\nRadius: 1.0904 jupiter (11.965 earth or 76,232 km)\nTemperature: -23.57°C (249.58 K)\nStellar flux: 85.67% as earth",font="NewComputerModern10").move_to([19.5,0.8015*3,0]).scale(0.4)
        Enecune_Wiki = Text("Enecune\nCold jupiter\nSemi-Major Axis: 13.51 AU (2.0211 B km)\nOrbital Period: 40.84 years (14,907.42 days)\nEccentricity:0.057\nMass: 1.235 jupiter (392.51 earth)\nRadius: 0.9987 jupiter (10.959 earth or 69,822 km)\nTemperature: -103.58°C (169.57 K)\nStellar flux: 3.9612% as earth",font="NewComputerModern10").move_to([24.7,0.734*3,0]).scale(0.367)
        self.add(Mate_Wiki)
        self.wait(4)
        self.play(FadeOut(Mate_Wiki))
        self.play(self.camera.frame.animate.scale(1.603).move_to([22,0.8015*3,0]),Mate_Wiki_Comparsion.animate.shift(10*LEFT)) # zoom 0.8015x out
        self.wait(0.5)
        self.add(Scipli_Wiki)
        self.wait(4)
        self.play(FadeOut(Scipli_Wiki))
        self.play(self.camera.frame.animate.scale(0.91578).move_to([27,0.734*3,0]),Scipli_Wiki_Comparsion.animate.shift(10*LEFT)) # zoom 0.7339x out
        self.wait(0.5)
        self.add(Enecune_Wiki)
        self.wait(4)
        self.play(FadeOut(Enecune_Wiki))
        self.wait(1)

        # CLEAR BEFORE ADD
        self.camera.frame_height = 8
        self.camera.frame_width = 8 * 16/9
        self.camera.frame.move_to(ORIGIN)
        self.remove(Mate_Wiki_Comparsion,Scipli_Wiki_Comparsion,Enecune_Wiki_Comparsion)

        # PLANET SURFACE
        Fertumi_Base_View = Dot(radius=0.02192,color=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_Glow_View = create_glow(Fertumi_Base_View,rad=0.02192*80,col=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_View = VGroup(Fertumi_Base_View,Fertumi_Glow_View).shift(3*RIGHT)
        Mate_Surface = Dot(radius=3,color=BLUE_A)
        planet_shadow = VGroup(Circle(radius=3,stroke_width=0,fill_color=BLACK,fill_opacity=0.7-idx/10).move_to(Mate_Surface).shift((3.5+idx/50)*LEFT) for idx in range(50))
        Scipli_Surface = Dot(radius=3,color=GOLD_B)
        Enecune_Surface = Dot(radius=3,color=YELLOW_A)
        self.add(Mate_Surface)
        self.wait(4)
        Mate_Surface.shift(3*LEFT)
        self.add(Fertumi_View,planet_shadow)
        self.wait(4)
        self.remove(Fertumi_View,planet_shadow,Mate_Surface)
        self.add(Scipli_Surface)
        self.wait(4)
        Scipli_Surface.shift(3*LEFT)
        Fertumi_View.scale(0.1504)
        self.add(Fertumi_View,planet_shadow)
        self.wait(4)
        self.remove(Fertumi_View,planet_shadow,Scipli_Surface)
        self.add(Enecune_Surface)
        self.wait(4)
        Enecune_Surface.shift(3*LEFT)
        Fertumi_View.scale(0.215)
        self.add(Fertumi_View,planet_shadow)
        self.wait(4)
        
        # CLEAR OUT
        self.remove(Fertumi_View,planet_shadow,Enecune_Surface)

        # PART 3
        self.add(zone,star_base,star_glow)
        self.add(Mate_orbit,Scipli_orbit,Enecune_orbit)
        self.add(lum_text_x,lum_num_x,time_text_x,time_million_x,temperature_text_x,temperature_num_x,radius_text_x,radius_num_x,mass_text_x,mass_num_x)
        self.add(star_info_text_x,Mate_info_text_x,Scipli_info_text_x,Enecune_info_text_x,sq_info_x,Mate_base_x,Scipli_base_x,Enecune_base_x,star_info_x)
        t.add_updater(lambda mob,dt: mob.increment_value(30e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-240*dt))
        self.wait(77/3)

        # CLEAR UPDATER
        rotate_deg.clear_updaters()
        t.clear_updaters()
        self.wait(0.1)        
        self.remove(star_info_text_x,Mate_info_text_x,Scipli_info_text_x,Enecune_info_text_x,sq_info_x,Mate_base_x,Scipli_base_x,Enecune_base_x,star_info_x)
        self.remove(Mate_orbit,Scipli_orbit,Enecune_orbit)
        self.remove(lum_text_x,lum_num_x,time_text_x,time_million_x,temperature_text_x,temperature_num_x,radius_text_x,radius_num_x,mass_text_x,mass_num_x)
        self.remove(zone,star_base,star_glow)

        # TEMPERATURE BEFORE STAR RUN OUT HYDROGEN
        Mate_Wiki_Comparsion.move_to([-5,0,0])
        Scipli_Wiki_Comparsion.move_to(ORIGIN)
        Enecune_Wiki_Comparsion.move_to([5,0,0])
        temperature_c = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_k = Text("Temperature in kelvin",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_mate_c = Text("364.01°C",font="NewComputerModern10").next_to(Mate_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_scipli_c = Text("-20.89°C",font="NewComputerModern10").next_to(Scipli_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_enecune_c = Text("-98.04°C",font="NewComputerModern10").next_to(Enecune_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_mate_k = Text("637.16 K",font="NewComputerModern10").next_to(Mate_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_scipli_k = Text("252.26 K",font="NewComputerModern10").next_to(Scipli_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_enecune_k = Text("175.11 K",font="NewComputerModern10").next_to(Enecune_Wiki_Comparsion,DOWN).scale(0.5)
        self.add(Mate_Wiki_Comparsion,Scipli_Wiki_Comparsion,Enecune_Wiki_Comparsion,temperature_c,temperature_mate_c,temperature_scipli_c,temperature_enecune_c)
        self.wait(4)
        self.play(Transform(temperature_mate_c,temperature_mate_k),Transform(temperature_scipli_c,temperature_scipli_k),Transform(temperature_enecune_c,temperature_enecune_k),ReplacementTransform(temperature_c,temperature_k))
        self.wait(3)

        # CLEAR OUT
        self.remove(temperature_enecune_k,temperature_mate_k,temperature_scipli_k,Mate_Wiki_Comparsion,Scipli_Wiki_Comparsion,Enecune_Wiki_Comparsion,temperature_k)

        # COMPARSION LATE MAIN SEQUENCE
        Fertumi_comparsion_late = Dot(radius=2.38,fill_color=ManimColor.from_rgb((255, 251, 245)))
        Fertumi_comparsion_late_glow = create_glow(Fertumi_comparsion_late,rad=2.38*3,col=ManimColor.from_rgb((255, 251, 245)))
        Fertumi_late = VGroup(Fertumi_comparsion_late,Fertumi_comparsion_late_glow).shift(RIGHT*3+UP*2.38)
        self.camera.frame.shift(3*UP)
        Fertumi_text.next_to(Fertumi_comparsion_late,UP)
        self.add(Fertumi_late,Sol,Sol_text,Fertumi_text)
        self.wait(3)

class TimelineRedGiant(ZoomedScene):
    def construct(self):
        # THE FUNCTION
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        def planet_hot_glow_2200c(vmobject, rad=1, col=YELLOW_D): # if planet is very hot, it glows a lot, shift to shorter wavelength again by wien laws
            glow_group = VGroup(Annulus(
                inner_radius=0.95*rad*(1.01**(idx)),
                outer_radius=1.05*rad*(1.01**(idx)), 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        def planet_hot_glow_1500c(vmobject, rad=1, col=ORANGE): # it glows, shift to shorter wavelength
            glow_group = VGroup(Annulus(
                inner_radius=0.95*rad*(1.01**(idx)),
                outer_radius=1.05*rad*(1.01**(idx)), 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        def planet_hot_glow_650c(vmobject, rad=1, col="#FF5000"): # if planet is hot about 650 c, it glows a bit does to it emit some visible light
            glow_group = VGroup(Annulus(
                inner_radius=0.95*rad*(1.01**(idx)),
                outer_radius=1.05*rad*(1.01**(idx)), 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(40)).move_to(vmobject)
            return glow_group
        def hz(lum=1): # Habitable zone radius is AU and luminosity is Sun
            inter = Annulus(inner_radius=0.79*lum**0.5, outer_radius=0.93*lum**0.5,fill_color= YELLOW,fill_opacity=0.2,stroke_width=0) # inner habitable zone
            hab = Annulus(inner_radius=0.93*lum**0.5, outer_radius=1.45*lum**0.5,fill_color= GREEN,fill_opacity=0.2,stroke_width=0)   
            outer = Annulus(inner_radius=1.45*lum**0.5, outer_radius=1.63*lum**0.5,fill_color= BLUE_B,fill_opacity=0.2,stroke_width=0) # outer habitable zone
            zone = VGroup(inter,hab,outer)
            return zone    
        def planet(earth=1,col="#423f50"): # Earth radius to AU
            size = Dot(radius=earth*4.26354e-5,fill_color=col)
            return size
        def star(sun=1,col="#423f50"): # Sun radius to AU
            size = Dot(radius=sun*0.0046524726,fill_color=col)
            return size
        def orbit(w=1,h=1,col=RED): # Orbit of planet
            orb = Ellipse(width=w*2,height=h*2,stroke_width=h,color=col)
            return orb
        def decimal_value(x):
            number_place = int(max(-np.log10(x) + 3,0))
            return number_place
        def luminosity(): # luminosity is Sun
            time = t.get_value()
            if t.get_value() <= -2e7:
                return 59.86311
            elif -2e7 < t.get_value() <= 0:
                return 0.89 + np.exp(4.077-(time/1e6+20)) + np.exp(time/3e6+1.33)
            elif 0 < t.get_value() <= 2.8e9:
                return 4.67 + (1.48 ** 3.5)*1e-10*3.21*time
            elif 2.8e9 < t.get_value() <= 2.85e9:
                return 8.2146 + (time-2.8e9)*4.72e-8
            elif 2.85e9 < t.get_value() <= 2.93e9:
                return 10.5746 - (time-2.85e9)*4.4e-8
            elif 2.93e9 < t.get_value() <= 3.06e9:
                return 7.0546 * np.exp((time-2.93e9)/5e7)
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 94.98128 * np.exp((time-3.06e9)/6e6)
            elif 3.08e9 < t.get_value() <= 3.1e9:
                return 62.34 * np.exp((time-3.08e9)/1e9)
            elif 3.1e9 < t.get_value() <= 3.2e9:
                return 63.5993 * np.exp((time-3.1e9)/1e8)
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 172.8808 * np.exp((time-3.2e9)/1.7e6)
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 2510.35208 * np.exp((time-3.205e9)/2.865e5)
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 2510.35208 * 1.0914394 * np.exp((time-3.2051e9)/2.865e5)
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 2510.35208 * 1.0914394**2 * np.exp((time-3.2052e9)/2.865e5)
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 2510.35208 * 1.0914394**3 * np.exp((time-3.2053e9)/2.865e5)    
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 2510.35208 * 1.0914394**4 * np.exp((time-3.2054e9)/2.865e5)      
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 2510.35208 * 1.0914394**5 * np.exp((time-3.2055e9)/2.865e5)  
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 2510.35208 * 1.0914394**6 * np.exp((time-3.2056e9)/2.865e5)      
            elif 3.2057e9 < t.get_value() <= 3.20673e9:
                return 6016.1503 / np.exp((time-3.2057e9)/1e5)
            elif 3.20673e9 < t.get_value() <= 3.37e9:
                return 0.2023417 / np.exp(np.log10((time-3.20673e9)/1e5+0.1)+1)
            else:
                return 0.0029952 / np.exp(np.log((time-3.37e9)/1e8+1))                                                     
        def radius(): # radius is Sun
            time = t.get_value()
            if t.get_value() <= -2e7:
                return 15.749731
            elif -2e7 < t.get_value() <= 0:
                return 0.87 + np.exp(-17.3-(time/1e6)) + np.exp(time/1e7-0.6)
            elif 0 < t.get_value() <= 2.8e9:
                return 1.4188 * np.exp(time/5.4e9)
            elif 2.8e9 < t.get_value() <= 2.85e9:
                return 2.3829 * np.exp((time-2.8e9)/5e8)
            elif 2.85e9 < t.get_value() <= 2.93e9:
                return 2.633511 * np.exp((time-2.85e9)/3.35e8)
            elif 2.93e9 < t.get_value() <= 3.06e9:
                return 3.343853 * np.exp((time-2.93e9)/8.4e7)
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 15.71699 * np.exp((time-3.06e9)/1e7)
            elif 3.08e9 < t.get_value() <= 3.1e9:
                return 12.01 * np.exp((time-3.08e9)/1e9)
            elif 3.1e9 < t.get_value() <= 3.2e9:
                return 12.25 * np.exp((time-3.1e9)/1.85e8)
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 21.032449 * np.exp((time-3.2e9)/2.4e6)
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 140.652 * np.exp((time-3.205e9)/3e5)
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 140.652*1.07 * np.exp((time-3.2051e9)/3e5)
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 140.652*1.07**2 * np.exp((time-3.2052e9)/3e5)
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 140.652*1.07**3 * np.exp((time-3.2053e9)/3e5)
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 140.652*1.07**4 * np.exp((time-3.2054e9)/3e5)
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 140.652*1.07**5 * np.exp((time-3.2055e9)/3e5)
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 140.652*1.07**6 * np.exp((time-3.2056e9)/3e5)
            else:
                return 0.0131 + 294.58688 / np.exp((time-3.2057e9)/1.456e4)
        def temperature(): # temperature of star
            return 5778*np.power(luminosity()/radius()**2,1./4)
        def color(): # Temperature to RGB and code from https://tannerhelland.com/2012/09/18/convert-temperature-rgb-algorithm-code.html
            temp = temperature() / 100
            if temp >= 67:
                r = 329.698727446046 * (temp-60)**-0.133204759227737
                g = 288.122169528293 * (temp-60)**-0.0755148492418579
                b = 255
            # exceed 255 or smaller than 0 will cause error become rgb must range 0 to 255
                r = min(max(0, r), 255)
                g = min(max(0, g), 255)
                b = min(max(0, b), 255)        
            else:
                r = 255    
                g = 99.4708025861262 * np.log(temp) - 161.119568166068
                g = min(max(0, g), 255)
                if temp < 20:
                    b = 0
                elif  20 <= temp <= 67:
                    b = 138.517761556144 * np.log(temp-10) - 305.044792730681
                    b = min(max(0, b), 255)
            return int(r),int(g),int(b)              
        def mass(): # Mass loss when red giant phase
            time = t.get_value()
            if -2e7 <= t.get_value() <= 3.06e9:
                return 1.48
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 1.48 - ((time-3.06e9)/8.5e7)**2
            elif 3.08e9 < t.get_value() <= 3.2e9:
                return 1.42463668
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 1.42463668 - ((time-3.2e9)/1.54e7)**2
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 1.31922261 - ((time-3.205e9)/3.075e5)**2
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 1.21346545 - ((time-3.2051e9)/3.075e5)**2
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 1.1077083 - ((time-3.2052e9)/3.075e5)**2
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 1.00195114 - ((time-3.2053e9)/3.075e5)**2
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 0.896193989 - ((time-3.2054e9)/3.075e5)**2
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 0.790436834 - ((time-3.2055e9)/3.075e5)**2      
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 0.684679679 - ((time-3.2056e9)/3.5e5)**2
            else:
                return 0.578922524
        def stellar_pulse(vmobject, rad=1, col=YELLOW_D): # stellar pulse
            glow_group = VGroup(Annulus(
                inner_radius=0.95*rad*(1.01**(idx)),
                outer_radius=1.05*rad*(1.01**(idx)), 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.05*np.sin(idx/60*PI/2)) for idx in range(60)).move_to(vmobject)
            return glow_group
        # BASE #        
        rotate_deg = ValueTracker(90) # this make orbit changing even when star become red giant does to planet orbit expanding while star lose mass
        t = ValueTracker(2790e6)
        place_num = 0

        # PART 3 RED GIANT
        
        lum_text_x = Text('Luminosity (Sun):',font="NewComputerModern10").move_to([-4.6,2.5,0]).scale(0.8)
        lum_num_x = always_redraw(lambda: DecimalNumber(luminosity(),num_decimal_places=decimal_value(luminosity())).next_to(lum_text_x,RIGHT,buff=0.6))
        time_text_x = Text('Million years:',font="NewComputerModern10").move_to([-5.1,3.2,0]).scale(0.8)
        time_million_x = always_redraw(lambda: DecimalNumber(t.get_value()/1e6,num_decimal_places=place_num).next_to(time_text_x,RIGHT,buff=0.6))
        temperature_text_x = Text('Temperature (K):',font="NewComputerModern10").move_to([-4.7,1.8,0]).scale(0.8)
        temperature_num_x = always_redraw(lambda: DecimalNumber(temperature(),num_decimal_places=0).next_to(temperature_text_x,RIGHT,buff=0.6))
        radius_text_x = Text('Radius (Sun):',font="NewComputerModern10").move_to([-5.1,1.1,0]).scale(0.8)
        radius_num_x = always_redraw(lambda: DecimalNumber(radius(),num_decimal_places=decimal_value(radius())).next_to(radius_text_x,buff=0.6))
        mass_text_x = Text('Mass (Sun):',font="NewComputerModern10").move_to([-5.35,0.4,0]).scale(0.8)
        mass_num_x = always_redraw(lambda: DecimalNumber(mass(),num_decimal_places=3).next_to(mass_text_x,buff=0.5))
        ## INFO ZOOM 1x ##
        sq_info_x = VGroup(Square(side_length=1.3,fill_opacity=1,fill_color=GRAY_E) for _ in range(4)).arrange(RIGHT,buff=0).move_to([-4.5,-3.3,0])
        star_base_info_x = always_redraw(lambda: Dot(radius=0.42,color=ManimColor.from_rgb(color())).move_to(sq_info_x[0]))
        star_glow_info_x = always_redraw(lambda: create_glow(star_base_info_x,rad=0.42*3,col=ManimColor.from_rgb(color())))
        star_info_x = VGroup(star_base_info_x,star_glow_info_x)
        Mate_base_x = Dot(radius=0.35,fill_color=BLUE_A).move_to(sq_info_x[1])
        Mate_hot_glow_x_650c = planet_hot_glow_650c(Mate_base_x,rad=0.35).scale(1)
        Mate_hot_glow_x_1500c = planet_hot_glow_1500c(Mate_base_x,rad=0.35).scale(1)
        Mate_hot_glow_x_2200c = planet_hot_glow_2200c(Mate_base_x,rad=0.35).scale(1)
        Scipli_base_x = Dot(radius=0.35,fill_color=GOLD_B).move_to(sq_info_x[2])
        Scipli_hot_glow_x_650c = planet_hot_glow_650c(Scipli_base_x,rad=0.35).scale(1)
        Enecune_base_x = Dot(radius=0.35,fill_color=YELLOW_A).move_to(sq_info_x[3])
        Enecune_hot_glow_x = planet_hot_glow_1500c(Enecune_base_x,rad=0.35).scale(1)
        # INFO TEXT ZOOM 1x #
        star_info_text_x = Text("Fertumi",font="NewComputerModern10").next_to(sq_info_x[0],UP,buff=0.1).scale(0.4)
        Mate_info_text_x = Text("Mate",font="NewComputerModern10").next_to(sq_info_x[1],UP,buff=0.1).scale(0.4)
        Scipli_info_text_x = Text("Scipli",font="NewComputerModern10").next_to(sq_info_x[2],UP,buff=0.1).scale(0.4)
        Enecune_info_text_x = Text("Enecune",font="NewComputerModern10").next_to(sq_info_x[3],UP,buff=0.1).scale(0.4)

        ## ORBIT ##
        Mate_orbit = always_redraw(lambda: orbit(w=0.448*(1.48/mass()),h=0.437*(1.48/mass()),col=GRAY_A).move_to([0.0113*(1.48/mass()),0,0]).rotate((rotate_deg.get_value()+60)*DEGREES,about_point=ORIGIN))
        Scipli_orbit = always_redraw(lambda: orbit(w=2.98*(1.48/mass()),h=2.905*(1.48/mass()),col=GOLD_B).move_to([0.07829*(1.48/mass()),0,0]).rotate((rotate_deg.get_value()+120)*DEGREES,about_point=ORIGIN))
        Enecune_orbit = always_redraw(lambda: orbit(w=14.3*(1.48/mass()),h=13.45*(1.48/mass()),col=YELLOW_A).move_to([0.807*(1.48/mass()),0,0]).rotate((rotate_deg.get_value()-50)*DEGREES,about_point=ORIGIN))

        ## STAR AND HABITABLE ZONE ##
        zone = always_redraw(lambda: hz(lum=luminosity()))
        star_base = always_redraw(lambda: star(sun=radius(),col=ManimColor.from_rgb(color())))
        star_glow = always_redraw(lambda: create_glow(star_base,rad=10*0.0046524726*radius(),col=ManimColor.from_rgb(color())))
        
        # ADD
        self.add(t,rotate_deg)
        self.add(zone,star_base,star_glow)
        self.add(Mate_orbit,Scipli_orbit,Enecune_orbit)
        self.add(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.add(sq_info_x,star_info_x,Mate_base_x,Scipli_base_x,Enecune_base_x)
        self.add(star_info_text_x,Mate_info_text_x,Scipli_info_text_x,Enecune_info_text_x)

        t.add_updater(lambda mob,dt: mob.increment_value(5e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-40*dt))
        hydrogen_run_out = Text("Hydrogen run out in Fertumi core",font="NewComputerModern10").scale(0.6).next_to(sq_info_x[3],RIGHT)
        core_enough_temperature = Text("Fertumi core is hot enough to fuse helium",font="NewComputerModern10").scale(0.6).next_to(sq_info_x[3],RIGHT)
        # DIALOG
        round_rectangle = RoundedRectangle(corner_radius=0.1)
        chemistry = MathTex(r"^{1}{{H}}").set_color(BLUE_B).move_to([-1,0,0]).scale(2)  
        warning_triangle = Triangle().set_color(RED).scale(0.6)
        warning_sign = Text("!").set_color(RED).move_to(warning_triangle)
        warning = VGroup(warning_triangle,warning_sign).next_to(chemistry,buff=1)
        arrow_down = Polygram([[-1,-1,0],[-1.5,-2,0],[-1.7,-1,0]]).set_color(WHITE)   
        dialog_hydrogen_out = VGroup(round_rectangle,chemistry,warning,arrow_down).scale(0.5).move_to([-6,-1.5,0]) 

        self.wait(12) # 2850 My
        self.add(dialog_hydrogen_out,hydrogen_run_out)
        self.wait(4) # 2870 My
        self.remove(dialog_hydrogen_out,hydrogen_run_out)
        self.wait(28) # 3010 My
        Mate_base_x.set_color("#e3b790"),self.add(Mate_hot_glow_x_650c)
        self.wait(11) # 3065 My
        Mate_base_x.set_color(ORANGE),self.add(Mate_hot_glow_x_1500c),self.remove(Mate_hot_glow_x_650c)
        self.wait(1.6) # 3073 My
        Scipli_base_x.set_color("#fe9240"),self.add(Scipli_hot_glow_x_650c)
        self.wait(0.4) # 3075 My
        Mate_base_x.set_color(YELLOW_D),self.add(Mate_hot_glow_x_2200c),self.remove(Mate_hot_glow_x_1500c)
        self.wait(0.6) # 3078 My
        self.play(FadeOut(Mate_base_x,Mate_orbit,Mate_hot_glow_x_2200c,Mate_info_text_x,sq_info_x[1]),run_time=0.4) # 3080 My
        pulse_1 = stellar_pulse(ORIGIN,rad=0.5582)
        pulse_1.add_updater(lambda mob,dt: mob.scale(1.2))
        self.add(pulse_1,core_enough_temperature)
        self.wait(0.8) # 3084 My
        self.remove(pulse_1,Scipli_hot_glow_x_650c)
        Scipli_base_x.set_color(GOLD_B)
        self.wait(0.2) # 3085 My

        ## CLEAR
        t.clear_updaters()
        rotate_deg.clear_updaters()
        self.remove(zone,star_base,star_glow)
        self.remove(Scipli_orbit,Enecune_orbit)
        self.remove(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.remove(sq_info_x[0],sq_info_x[2],sq_info_x[3],star_info_x,Scipli_base_x,Enecune_base_x,core_enough_temperature)
        self.remove(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x)

        ## COMPARSION
        Fertumi_comparsion = Dot(radius=12.1,fill_color=ManimColor.from_rgb((255, 221, 194)))
        Fertumi_comparsion_glow = create_glow(Fertumi_comparsion,rad=12.1*3,col=ManimColor.from_rgb((255, 221, 194)))
        Fertumi = VGroup(Fertumi_comparsion,Fertumi_comparsion_glow).shift(RIGHT*8+UP*12.1)
        Sol_comparsion = Dot(radius=1,fill_color=ManimColor.from_rgb((255, 242, 230)))
        Sol_comparsion_glow = create_glow(Sol_comparsion,rad=1*3,col=ManimColor.from_rgb((255, 242, 230)))
        Sol = VGroup(Sol_comparsion,Sol_comparsion_glow).shift(LEFT*9+UP)
        self.camera.frame.scale(4).shift(12*UP)
        Sol_text = Text("Sol",font="NewComputerModern10").next_to(Sol_comparsion,UP)
        Fertumi_text = Text("Fertumi",font="NewComputerModern10").next_to(Fertumi_comparsion,UP,buff=2).scale(3)
        self.add(Fertumi,Sol,Sol_text,Fertumi_text)
        self.wait(4)

        ## CLEAR OUT
        self.remove(Fertumi,Sol,Sol_text,Fertumi_text)
        self.camera.frame.scale(1/4).move_to(ORIGIN)

        ## TEMPERATURE RED GIANT PHASE
        Scipli_RedGiant = Dot(radius=1.602,color=GOLD_B).move_to([-3,0,0])
        Enecune_RedGiant = Dot(radius=1.467,color=YELLOW_A).move_to([3,0,0])
        temperature_c = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_k = Text("Temperature in kelvin",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_scipli_c = Text("138.84°C",font="NewComputerModern10").next_to(Scipli_RedGiant,DOWN).scale(0.5)
        temperature_enecune_c = Text("-63.42°C",font="NewComputerModern10").next_to(Enecune_RedGiant,DOWN).scale(0.5)
        temperature_scipli_k = Text("411.99 K",font="NewComputerModern10").next_to(Scipli_RedGiant,DOWN).scale(0.5)
        temperature_enecune_k = Text("209.73 K",font="NewComputerModern10").next_to(Enecune_RedGiant,DOWN).scale(0.5)
        self.add(Scipli_RedGiant,Enecune_RedGiant,temperature_c,temperature_scipli_c,temperature_enecune_c)
        self.wait(3)
        self.play(ReplacementTransform(temperature_c,temperature_k),ReplacementTransform(temperature_scipli_c,temperature_scipli_k),ReplacementTransform(temperature_enecune_c,temperature_enecune_k))
        self.wait(2)

        ## CLEAR OUT
        self.remove(Scipli_RedGiant,Enecune_RedGiant,temperature_k,temperature_scipli_k,temperature_enecune_k)
        
        ## ADD
        self.add(zone,star_base,star_glow)
        self.add(Scipli_orbit,Enecune_orbit)
        self.add(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.add((sq_info_x-sq_info_x[1]),star_info_x,Scipli_base_x,Enecune_base_x)
        self.add(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x)
        self.add(core_enough_temperature)
        t.add_updater(lambda mob,dt: mob.increment_value(5e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-40*dt))
        VGroup(sq_info_x[2:4],Scipli_base_x,Enecune_base_x,Scipli_info_text_x,Enecune_info_text_x,core_enough_temperature,Scipli_hot_glow_x_650c).shift(LEFT*1.3)
        self.wait(2) # 3095 My
        self.play(FadeOut(core_enough_temperature)) # 3100 My
        self.wait(16) # 3180 My

        ## HELIUM RUN OUT
        round_rectangle = RoundedRectangle(corner_radius=0.1)
        chemistry = MathTex(r"^{4}{{He}}").set_color(GREEN_C).move_to([-1,0,0]).scale(1.5)  
        warning_triangle = Triangle().set_color(RED).scale(0.6)
        warning_sign = Text("!").set_color(RED).move_to(warning_triangle)
        warning = VGroup(warning_triangle,warning_sign).next_to(chemistry,buff=1)
        arrow_down = Polygram([[-1,-1,0],[-1.5,-2,0],[-1.7,-1,0]]).set_color(WHITE)   
        dialog_helium_out = VGroup(round_rectangle,chemistry,warning,arrow_down).scale(0.5).move_to([-6,-1.5,0])

        helium_out = Text("Helium run out in Fertumi core and fuse carbon",font="NewComputerModern10").scale(0.6).next_to(sq_info_x[3],RIGHT)
        self.add(dialog_helium_out,helium_out)

        self.wait(2) # 3190 My
        self.remove(dialog_helium_out,helium_out)
        self.wait(2) # 3200 My
        ## SET SPEED
        place_num = 1
        t.clear_updaters()
        rotate_deg.clear_updaters()
        t.add_updater(lambda mob,dt: mob.increment_value(500e3*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-8*dt))

        self.wait(8) # 3204 My
        Scipli_base_x.set_color("#fe9240"),self.add(Scipli_hot_glow_x_650c)
        self.wait(1.8) # 3204.9 My

        ## SET SPEED
        place_num = 2
        t.clear_updaters()
        t.add_updater(lambda mob,dt: mob.increment_value(50e3*dt))
        self.wait(2) # 3205 My

        pulse_agb = [stellar_pulse(ORIGIN,rad=0.7816*1.07**i) for i in range(9)]
        self.add(pulse_agb[0])
        pulse_agb[0].add_updater(lambda mob,dt: mob.scale(1.2))
        for i in range(7):
            self.wait(2) # 3205 My to 3205.7 My
            self.remove(pulse_agb[i])
            self.add(pulse_agb[i+1])
            pulse_agb[i+1].add_updater(lambda mob,dt: mob.scale(1.2))
        self.remove(pulse_agb[7])
        self.add(pulse_agb[8])
        pulse_agb[8].add_updater(lambda mob,dt: mob.scale(1.2)) 
        
        self.wait(4) # 3205.9 My
        self.remove(pulse_agb[8])
        t.clear_updaters()
        t.add_updater(lambda mob,dt: mob.increment_value(500e3*dt))
        self.wait() # 3206.4 My
        Scipli_base_x.set_color(GOLD_B),self.remove(Scipli_hot_glow_x_650c)
        self.wait(3.2) # 3208 My

        ## CLEAR
        t.clear_updaters()
        rotate_deg.clear_updaters()
        self.remove(zone,star_base,star_glow)
        self.remove(Scipli_orbit,Enecune_orbit)
        self.remove(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.remove(sq_info_x[0],sq_info_x[2],sq_info_x[3],star_info_x,Scipli_base_x,Enecune_base_x)
        self.remove(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x)

        ## COMPARSION EARTH AND WHITE DWARF
        self.camera.frame.shift(3*UP)
        earth = SVGMobject("img\earth.svg").shift(UP+2*LEFT)
        Fertumi_white_dwarf_base = Dot(radius=1.429,fill_color=ManimColor.from_rgb((170, 198, 255)))
        Fertumi_white_dwarf_glow = create_glow(Fertumi_white_dwarf_base,rad=1.429*3,col=ManimColor.from_rgb((170, 198, 255)))
        Fertumi_white_dwarf = VGroup(Fertumi_white_dwarf_base,Fertumi_white_dwarf_glow).shift(1.429*UP+2*RIGHT)
        earth_text = Text("Earth",font="NewComputerModern10").next_to(earth,UP)
        Fertumi_text.next_to(Fertumi_white_dwarf_base,UP).scale(1/3)
        radius_note = MathTex(r"1.429 \ R_{E}").move_to([-6,6.5,0])
        self.add(earth,Fertumi_white_dwarf,earth_text,Fertumi_text,radius_note)
        self.wait(5)

class TimelineWhiteDwarf(ZoomedScene):
    def construct(self):
        ## FUNCTION
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        def hz(lum=1): # Habitable zone radius is AU and luminosity is Sun
            inter = Annulus(inner_radius=0.79*lum**0.5, outer_radius=0.93*lum**0.5,fill_color= YELLOW,fill_opacity=0.2,stroke_width=0) # inner habitable zone
            hab = Annulus(inner_radius=0.93*lum**0.5, outer_radius=1.45*lum**0.5,fill_color= GREEN,fill_opacity=0.2,stroke_width=0)   
            outer = Annulus(inner_radius=1.45*lum**0.5, outer_radius=1.63*lum**0.5,fill_color= BLUE_B,fill_opacity=0.2,stroke_width=0) # outer habitable zone
            zone = VGroup(inter,hab,outer)
            return zone    
        def planet(earth=1,col="#423f50"): # Earth radius to AU
            size = Dot(radius=earth*4.26354e-5,fill_color=col)
            return size
        def star(sun=1,col="#423f50"): # Sun radius to AU
            size = Dot(radius=sun*0.0046524726,fill_color=col)
            return size
        def orbit(w=1,h=1,col=RED): # Orbit of planet
            orb = Ellipse(width=w*2,height=h*2,stroke_width=h,color=col)
            return orb
        def decimal_value(x):
            number_place = int(max(-np.log10(x) + 3,0))
            return number_place
        def luminosity(): # luminosity is Sun
            time = t.get_value()
            if t.get_value() <= -2e7:
                return 59.86311
            elif -2e7 < t.get_value() <= 0:
                return 0.89 + np.exp(4.077-(time/1e6+20)) + np.exp(time/3e6+1.33)
            elif 0 < t.get_value() <= 2.8e9:
                return 4.67 + (1.48 ** 3.5)*1e-10*3.21*time
            elif 2.8e9 < t.get_value() <= 2.85e9:
                return 8.2146 + (time-2.8e9)*4.72e-8
            elif 2.85e9 < t.get_value() <= 2.93e9:
                return 10.5746 - (time-2.85e9)*4.4e-8
            elif 2.93e9 < t.get_value() <= 3.06e9:
                return 7.0546 * np.exp((time-2.93e9)/5e7)
            elif 3.06e9 < t.get_value() <= 3.08e9:
                return 94.98128 * np.exp((time-3.06e9)/6e6)
            elif 3.08e9 < t.get_value() <= 3.1e9:
                return 62.34 * np.exp((time-3.08e9)/1e9)
            elif 3.1e9 < t.get_value() <= 3.2e9:
                return 63.5993 * np.exp((time-3.1e9)/1e8)
            elif 3.2e9 < t.get_value() <= 3.205e9:
                return 172.8808 * np.exp((time-3.2e9)/1.7e6)
            elif 3.205e9 < t.get_value() <= 3.2051e9:
                return 2510.35208 * np.exp((time-3.205e9)/2.865e5)
            elif 3.2051e9 < t.get_value() <= 3.2052e9:
                return 2510.35208 * 1.0914394 * np.exp((time-3.2051e9)/2.865e5)
            elif 3.2052e9 < t.get_value() <= 3.2053e9:
                return 2510.35208 * 1.0914394**2 * np.exp((time-3.2052e9)/2.865e5)
            elif 3.2053e9 < t.get_value() <= 3.2054e9:
                return 2510.35208 * 1.0914394**3 * np.exp((time-3.2053e9)/2.865e5)    
            elif 3.2054e9 < t.get_value() <= 3.2055e9:
                return 2510.35208 * 1.0914394**4 * np.exp((time-3.2054e9)/2.865e5)      
            elif 3.2055e9 < t.get_value() <= 3.2056e9:
                return 2510.35208 * 1.0914394**5 * np.exp((time-3.2055e9)/2.865e5)  
            elif 3.2056e9 < t.get_value() <= 3.2057e9:
                return 2510.35208 * 1.0914394**6 * np.exp((time-3.2056e9)/2.865e5)      
            elif 3.2057e9 < t.get_value() <= 3.20673e9:
                return 6016.1503 / np.exp((time-3.2057e9)/1e5)
            elif 3.20673e9 < t.get_value() <= 3.37e9:
                return 0.2023417 / np.exp(np.log10((time-3.20673e9)/1e5+0.1)+1)
            else:
                return 0.0029952 / np.exp(np.log((time-3.37e9)/1e8+1))                                                     
        def temperature(): # temperature of star
            return 5778*np.power(luminosity()/0.0131**2,1./4)
        def color(): # Temperature to RGB and code from https://tannerhelland.com/2012/09/18/convert-temperature-rgb-algorithm-code.html
            temp = temperature() / 100
            if temp >= 67:
                r = 329.698727446046 * (temp-60)**-0.133204759227737
                g = 288.122169528293 * (temp-60)**-0.0755148492418579
                b = 255
            # exceed 255 or smaller than 0 will cause error become rgb must range 0 to 255
                r = min(max(0, r), 255)
                g = min(max(0, g), 255)
                b = min(max(0, b), 255)        
            else:
                r = 255    
                g = 99.4708025861262 * np.log(temp) - 161.119568166068
                g = min(max(0, g), 255)
                if temp < 20:
                    b = 0
                elif  20 <= temp <= 67:
                    b = 138.517761556144 * np.log(temp-10) - 305.044792730681
                    b = min(max(0, b), 255)
            return int(r),int(g),int(b)
        # BASE #        
        rotate_deg = ValueTracker(90) # this make orbit changing even when star become red giant does to planet orbit expanding while star lose mass
        t = ValueTracker(3208e6)
        place_num = 1
        # PART 4 THE END
        
        lum_text_x = Text('Luminosity (Sun):',font="NewComputerModern10").move_to([-4.6,2.5,0]).scale(0.8)
        lum_num_x = always_redraw(lambda: DecimalNumber(luminosity(),num_decimal_places=decimal_value(luminosity())).next_to(lum_text_x,RIGHT,buff=0.6))
        time_text_x = Text('Million years:',font="NewComputerModern10").move_to([-5.1,3.2,0]).scale(0.8)
        time_million_x = always_redraw(lambda: DecimalNumber(t.get_value()/1e6,num_decimal_places=place_num).next_to(time_text_x,RIGHT,buff=0.6))
        temperature_text_x = Text('Temperature (K):',font="NewComputerModern10").move_to([-4.7,1.8,0]).scale(0.8)
        temperature_num_x = always_redraw(lambda: DecimalNumber(temperature(),num_decimal_places=0).next_to(temperature_text_x,RIGHT,buff=0.6))
        radius_text_x = Text('Radius (Earth):',font="NewComputerModern10").move_to([-4.9,1.1,0]).scale(0.8)
        radius_num_x = DecimalNumber(1.429,num_decimal_places=3).next_to(radius_text_x,buff=0.6)
        mass_text_x = Text('Mass (Sun):',font="NewComputerModern10").move_to([-5.35,0.4,0]).scale(0.8)
        mass_num_x = DecimalNumber(0.579,num_decimal_places=3).next_to(mass_text_x,buff=0.5)
        
        ## ORBIT
        Scipli_orbit = always_redraw(lambda: orbit(w=2.98*(1.48/0.5789),h=2.905*(1.48/0.5789),col=GOLD_B).move_to([0.07829*(1.48/0.5789),0,0]).rotate((rotate_deg.get_value()+120)*DEGREES,about_point=ORIGIN))
        Enecune_orbit = always_redraw(lambda: orbit(w=14.3*(1.48/0.5789),h=13.45*(1.48/0.5789),col=YELLOW_A).move_to([0.807*(1.48/0.5789),0,0]).rotate((rotate_deg.get_value()-50)*DEGREES,about_point=ORIGIN))

        ## STAR AND HABITABLE ZONE ##
        zone = always_redraw(lambda: hz(lum=luminosity()))
        star_base = always_redraw(lambda: star(sun=0.0131,col=ManimColor.from_rgb(color())))
        star_glow = always_redraw(lambda: create_glow(star_base,rad=10*0.0046524726*0.0131,col=ManimColor.from_rgb(color())))
         
        ## INFO ZOOM 1x ##
        sq_info_x = VGroup(Square(side_length=1.3,fill_opacity=1,fill_color=GRAY_E) for _ in range(3)).arrange(RIGHT,buff=0).move_to([-5.15,-3.3,0])
        star_base_info_x = always_redraw(lambda: Dot(radius=0.42,color=ManimColor.from_rgb(color())).move_to(sq_info_x[0]))
        star_glow_info_x = always_redraw(lambda: create_glow(star_base_info_x,rad=0.42*3,col=ManimColor.from_rgb(color())))
        star_info_x = VGroup(star_base_info_x,star_glow_info_x)
        Scipli_base_x = Dot(radius=0.35,fill_color=GOLD_B).move_to(sq_info_x[1])
        Enecune_base_x = Dot(radius=0.35,fill_color=YELLOW_A).move_to(sq_info_x[2])
        no_light_Scipli_x = Dot(radius=0.35,fill_color=BLACK).move_to(Scipli_base_x).set_opacity(0.2)
        no_light_Enecune_x = Dot(radius=0.35,fill_color=BLACK).move_to(Enecune_base_x).set_opacity(0.35)
        # INFO TEXT ZOOM 1x #
        star_info_text_x = Text("Fertumi",font="NewComputerModern10").next_to(sq_info_x[0],UP,buff=0.1).scale(0.4)
        Scipli_info_text_x = Text("Scipli",font="NewComputerModern10").next_to(sq_info_x[1],UP,buff=0.1).scale(0.4)
        Enecune_info_text_x = Text("Enecune",font="NewComputerModern10").next_to(sq_info_x[2],UP,buff=0.1).scale(0.4)
        
        # ADD
        self.add(t,rotate_deg)
        self.add(zone,star_base,star_glow)
        self.add(Scipli_orbit,Enecune_orbit)
        self.add(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.add(sq_info_x,star_info_x,Scipli_base_x,Enecune_base_x)
        self.add(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x)
        t.add_updater(lambda mob,dt: mob.increment_value(2e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-30*dt))
        self.wait(2) # 3212 My
        self.add(no_light_Enecune_x)
        self.wait(8) # 3228 My

        ## CLEAR OUT
        self.remove(zone,star_base,star_glow)
        self.remove(Scipli_orbit,Enecune_orbit)
        self.remove(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.remove(sq_info_x,star_info_x,Scipli_base_x,Enecune_base_x)
        self.remove(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x)
        t.clear_updaters()
        rotate_deg.clear_updaters()

        ## TEMPERATURE AND MASS
        Scipli_WhiteDwarf = Dot(radius=1.594,color=GOLD_B).move_to([-3,0,0])
        Enecune_WhiteDwarf = Dot(radius=1.464,color=YELLOW_A).move_to([3,0,0])
        no_light_Scipli_WhiteDwarf = Dot(radius=1.594,fill_color=BLACK).move_to(Scipli_WhiteDwarf).set_opacity(0.2)
        no_light_Enecune_WhiteDwarf = Dot(radius=1.464,fill_color=BLACK).move_to(Enecune_WhiteDwarf).set_opacity(0.35)
        # Mass
        mass = Text("Mass",font="NewComputerModern10").to_edge(UP).scale(0.8)
        mass_scipli = MathTex(r"2.4885 \ M_{J}").next_to(Scipli_WhiteDwarf,DOWN).scale(0.7)
        mass_enecune = MathTex(r"1.2347 \ M_{J}").next_to(Enecune_WhiteDwarf,DOWN).scale(0.7)
        # Temperature
        temperature_c = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_k = Text("Temperature in kelvin",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_scipli_c = Text("-132.48°C",font="NewComputerModern10").next_to(Scipli_WhiteDwarf,DOWN).scale(0.5)
        temperature_enecune_c = Text("-154.79°C",font="NewComputerModern10").next_to(Enecune_WhiteDwarf,DOWN).scale(0.5)
        temperature_scipli_k = Text("140.67 K",font="NewComputerModern10").next_to(Scipli_WhiteDwarf,DOWN).scale(0.5)
        temperature_enecune_k = Text("118.36 K",font="NewComputerModern10").next_to(Enecune_WhiteDwarf,DOWN).scale(0.5)
        self.add(Scipli_WhiteDwarf,Enecune_WhiteDwarf,mass,mass_scipli,mass_enecune,no_light_Enecune_WhiteDwarf)  
        self.wait(3)
        self.play(ReplacementTransform(mass,temperature_c),ReplacementTransform(mass_scipli,temperature_scipli_c),ReplacementTransform(mass_enecune,temperature_enecune_c)) 
        self.wait(2)
        self.play(ReplacementTransform(temperature_c,temperature_k),ReplacementTransform(temperature_scipli_c,temperature_scipli_k),ReplacementTransform(temperature_enecune_c,temperature_enecune_k))
        self.wait(2)


        ## CLEAR
        self.remove(temperature_k,temperature_scipli_k,temperature_enecune_k,no_light_Enecune_WhiteDwarf,Scipli_WhiteDwarf,Enecune_WhiteDwarf)
        ## ADD
        self.add(zone,star_base,star_glow)
        self.add(Scipli_orbit,Enecune_orbit)
        self.add(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.add(sq_info_x,star_info_x,Scipli_base_x,Enecune_base_x)
        self.add(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x)
        self.add(no_light_Enecune_x)
        place_num = 0
        t.add_updater(lambda mob,dt: mob.increment_value(20e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-120*dt))
        self.wait(8.6) # 3400 My
        
        t.clear_updaters()
        rotate_deg.clear_updaters()
        t.add_updater(lambda mob,dt: mob.increment_value(100e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-480*dt))
        self.wait(2) # 3600 My
        self.add(no_light_Scipli_x)
        no_light_Enecune_x.set_opacity(0.5)
        self.wait(4) # 4000 My
        self.play(FadeOut(zone),run_time=5) # 4500 My
        self.wait(2) # 4700 My
        no_light_Scipli_x.set_opacity(0.4)
        no_light_Enecune_x.set_opacity(0.6)
        self.wait(3) # 5000 My

        ## CLEAR
        self.remove(lum_num_x,lum_text_x,temperature_text_x,temperature_num_x,time_million_x,time_text_x,radius_num_x,radius_text_x,mass_text_x,mass_num_x)
        self.remove(sq_info_x,star_info_x,Scipli_base_x,Enecune_base_x)
        self.remove(star_info_text_x,Scipli_info_text_x,Enecune_info_text_x,no_light_Enecune_x,no_light_Scipli_x)
        self.remove(star_base,star_glow)
        t.clear_updaters()
        rotate_deg.clear_updaters()

        ## ZOOM OUT
        self.camera.frame.scale(10)
        
        ## ZOOM 10x
        lum_text = Text('Luminosity (Sun):',font="NewComputerModern10").move_to([-4.6*10,2.5*10,0]).scale(0.8*10)
        lum_num = always_redraw(lambda: DecimalNumber(luminosity(),num_decimal_places=decimal_value(luminosity())).next_to(lum_text,RIGHT,buff=16).scale(10))
        time_text = Text('Million years:',font="NewComputerModern10").move_to([-5.1*10,3.2*10,0]).scale(0.8*10)
        time_million = always_redraw(lambda: DecimalNumber(t.get_value()/1e6,num_decimal_places=place_num).next_to(time_text,RIGHT,buff=8).scale(10))
        temperature_text = Text('Temperature (K):',font="NewComputerModern10").move_to([-4.7*10,1.8*10,0]).scale(0.8*10)
        temperature_num = always_redraw(lambda: DecimalNumber(temperature(),num_decimal_places=0).next_to(temperature_text,RIGHT,buff=8).scale(10))
        radius_text = Text('Radius (Earth):',font="NewComputerModern10").move_to([-4.9*10,1.1*10,0]).scale(0.8*10)
        radius_num = always_redraw(lambda: DecimalNumber(1.429,num_decimal_places=3).next_to(radius_text,buff=6).scale(10))
        mass_text = Text('Mass (Sun):',font="NewComputerModern10").move_to([-5.35*10,0.4*10,0]).scale(0.8*10)
        mass_num = always_redraw(lambda: DecimalNumber(0.579,num_decimal_places=3).next_to(mass_text,buff=6).scale(10))
        
        ## INFO ZOOM 10x ##
        sq_info = VGroup(Square(side_length=1.3*10,fill_opacity=1,fill_color=GRAY_E,stroke_width=DEFAULT_STROKE_WIDTH*10) for _ in range(3)).arrange(RIGHT,buff=0).move_to([-5.15*10,-3.3*10,0])
        star_base_info = always_redraw(lambda: Dot(radius=0.42*10,color=ManimColor.from_rgb(color())).move_to(sq_info[0]))
        star_glow_info = always_redraw(lambda: create_glow(star_base_info,rad=0.42*3*10,col=ManimColor.from_rgb(color())))
        star_info = VGroup(star_base_info,star_glow_info)
        Scipli_base = Dot(radius=0.35*10,fill_color=GOLD_B).move_to(sq_info[1])
        Enecune_base = Dot(radius=0.35*10,fill_color=YELLOW_A).move_to(sq_info[2])
        no_light_Scipli = Dot(radius=0.35*10,fill_color=BLACK).move_to(Scipli_base).set_opacity(0.4)
        no_light_Enecune = Dot(radius=0.35*10,fill_color=BLACK).move_to(Enecune_base).set_opacity(0.6)
        
        # INFO TEXT ZOOM 10x #
        star_info_text = Text("Fertumi",font="NewComputerModern10").next_to(sq_info[0],UP,buff=4).scale(4)
        Scipli_info_text = Text("Scipli",font="NewComputerModern10").next_to(sq_info[1],UP,buff=4).scale(4)
        Enecune_info_text = Text("Enecune",font="NewComputerModern10").next_to(sq_info[2],UP,buff=4).scale(4)
        
        # ADD
        self.add(lum_text,lum_num,time_text,time_million,temperature_text,temperature_num,radius_text,radius_num,mass_text,mass_num)
        self.add(sq_info,star_info,Scipli_base,Enecune_base,no_light_Scipli,no_light_Enecune)
        self.add(star_info_text,Scipli_info_text,Enecune_info_text)
        
        t.add_updater(lambda mob,dt: mob.increment_value(1000e6*dt))
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-360*6*dt))
        self.wait(4) # 9 By
        no_light_Scipli.set_opacity(0.6)
        no_light_Enecune.set_opacity(0.8)
        self.wait(5) # 14 By
        no_light_Scipli.set_opacity(0.7)
        no_light_Enecune.set_opacity(0.87)
        self.wait(5) # 19 By
        no_light_Scipli.set_opacity(0.75)
        no_light_Enecune.set_opacity(0.9)
        self.wait(6) # 25 By
        no_light_Scipli.set_opacity(0.8)
        no_light_Enecune.set_opacity(0.92)
        self.wait(5) # 30 By

        ## CLEAR
        t.clear_updaters()
        rotate_deg.clear_updaters()
        self.remove(lum_text,lum_num,time_text,time_million,temperature_text,temperature_num,radius_text,radius_num,mass_text,mass_num)
        self.remove(sq_info,star_info,Scipli_base,Enecune_base,no_light_Scipli,no_light_Enecune)
        self.remove(star_info_text,Scipli_info_text,Enecune_info_text)
        self.remove(Scipli_orbit,Enecune_orbit)
        self.camera.frame.scale(1/10)
        
        ## TEMPERATURE END
        no_light_Enecune_WhiteDwarf.set_opacity(0.85)
        no_light_Scipli_WhiteDwarf.set_opacity(0.8)
        temperature_c_end = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_k_end = Text("Temperature in kelvin",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_scipli_c_end = Text("-241.32°C",font="NewComputerModern10").next_to(Scipli_WhiteDwarf,DOWN).scale(0.5)
        temperature_enecune_c_end = Text("-249.85°C",font="NewComputerModern10").next_to(Enecune_WhiteDwarf,DOWN).scale(0.5)
        temperature_scipli_k_end = Text("31.83 K",font="NewComputerModern10").next_to(Scipli_WhiteDwarf,DOWN).scale(0.5)
        temperature_enecune_k_end = Text("23.3 K",font="NewComputerModern10").next_to(Enecune_WhiteDwarf,DOWN).scale(0.5)
        self.add(Scipli_WhiteDwarf,Enecune_WhiteDwarf,no_light_Enecune_WhiteDwarf,no_light_Scipli_WhiteDwarf,temperature_c_end,temperature_scipli_c_end,temperature_enecune_c_end)
        self.wait(2)
        self.play(ReplacementTransform(temperature_c_end,temperature_k_end),ReplacementTransform(temperature_scipli_c_end,temperature_scipli_k_end),ReplacementTransform(temperature_enecune_c_end,temperature_enecune_k_end))
        self.wait(2)
        
## WHEN I CREATE

class PlanetAndStarList(Scene):
    def construct(self):
        sq = VGroup(*[Square(side_length=1.3,fill_opacity=1,fill_color=BLACK) for _ in range(4)]).arrange(RIGHT,buff=0).move_to([-4.5,-3.3,0])
        self.add(sq)

class Comparsion(ZoomedScene):
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
            radius=rad*(1.002**(idx**2))/400, 
            stroke_opacity=0, 
            fill_color=col,
            fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        Fertumi_comparsion = Dot(radius=1.438,fill_color=ManimColor.from_rgb((238, 240, 255)))
        Fertumi_comparsion_glow = create_glow(Fertumi_comparsion,rad=1.438*3,col=ManimColor.from_rgb((238, 240, 255)))
        Fertumi = VGroup(Fertumi_comparsion,Fertumi_comparsion_glow).shift(RIGHT*3+UP*1.438)
        Sol_comparsion = Dot(radius=1,fill_color=ManimColor.from_rgb((255, 242, 230)))
        Sol_comparsion_glow = create_glow(Sol_comparsion,rad=1*3,col=ManimColor.from_rgb((255, 242, 230)))
        Sol = VGroup(Sol_comparsion,Sol_comparsion_glow).shift(LEFT*3+UP)
        self.camera.frame.shift(3*UP)
        Sol_text = Text("Sol",font="NewComputerModern10").next_to(Sol_comparsion,UP)
        Fertumi_text = Text("Fertumi",font="NewComputerModern10").next_to(Fertumi_comparsion,UP)
        self.add(Fertumi,Sol,Fertumi_text,Sol_text)

class TemperatureToRGB(Scene):
    def construct(self):
        temp = ValueTracker(1000)
        def color():
            temperature = temp.get_value() / 100
            if temperature >= 67:
                r = 329.698727446046 * (temperature-60)**-0.133204759227737
                g = 288.122169528293 * (temperature-60)**-0.0755148492418579
                b = 255
            # exceed 255 or smaller than 0 will cause error become rgb must range 0 to 255
                r = min(max(0, r), 255)
                g = min(max(0, g), 255)
                b = min(max(0, b), 255)        
            else:
                r = 255    
                g = 99.4708025861262 * np.log(temperature) - 161.119568166068
                g = min(max(0, g), 255)
                if temperature < 20:
                    b = 0
                elif  20 <= temperature <= 67:
                    b = 138.517761556144 * np.log(temperature-10) - 305.044792730681
                    b = min(max(0, b), 255)
            return int(r),int(g),int(b)        
        number = always_redraw(lambda: DecimalNumber(temp.get_value()).set_color(ManimColor.from_rgb(color())))
        self.add(number,temp)
        temp.add_updater(lambda mob,dt: mob.increment_value(1000*dt))
        self.wait(39)

class OrbitShrinkAndGrow(ZoomedScene):
    def construct(self):
        m = ValueTracker(1.48)
        rotate_deg = ValueTracker(0)
        def orbit(w=1,h=1,col=RED): # Orbit of planet
            orb = Ellipse(width=w*2,height=h*2,stroke_width=h,color=col)
            return orb
        Scipli_orbit = always_redraw(lambda: orbit(w=2.98*(1.48/m.get_value()),h=2.905*(1.48/m.get_value()),col=GOLD_B).move_to([0.07829*(1.48/m.get_value()),0,0]).rotate(rotate_deg.get_value()*DEGREES,about_point=ORIGIN))
        self.add(Scipli_orbit,rotate_deg)
        self.camera.frame.scale(2)        
        self.wait(1)
        rotate_deg.add_updater(lambda mob,dt: mob.increment_value(-3*360*dt))
        self.play(m.animate.set_value(1.44),run_time=2)
        self.play(m.animate.set_value(1.10),run_time=0.5)
        self.play(m.animate.set_value(1.01),run_time=0.5)
        self.play(m.animate.set_value(0.95),run_time=0.5)
        self.play(m.animate.set_value(0.86),run_time=0.5)
        self.play(m.animate.set_value(0.81),run_time=0.5)
        self.play(m.animate.set_value(0.77),run_time=0.5)
        self.play(m.animate.set_value(0.73),run_time=0.5)
        self.play(m.animate.set_value(0.68),run_time=0.5)
        self.play(m.animate.set_value(0.64),run_time=0.5)
        self.play(m.animate.set_value(0.58),run_time=0.5)
        self.wait(2)

class PlanetaryDisk(ZoomedScene):
    def construct(self):
        def disk(rad=1, col=RED_C):
            planetary = VGroup(Circle(radius=rad*1.1**idx,fill_opacity=0.01-idx/6000,fill_color=col,stroke_width=0) for idx in range(50))
            return planetary
        self.camera.frame.scale(5)
        planetary_disk = disk(rad=10)
        self.add(planetary_disk)   
            
class PlanetWiki(ZoomedScene):
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        self.camera.frame.scale(10).shift(30*UP)
        Fertumi_Base_Wiki_Comparsion = Dot(radius=30.121,color=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_Glow_Wiki_Comparsion = create_glow(Fertumi_Base_Wiki_Comparsion,rad=30.121*2,col=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_Wiki_Comparsion = VGroup(Fertumi_Base_Wiki_Comparsion,Fertumi_Glow_Wiki_Comparsion).move_to([-20,0,0]).shift(UP*30.121)
        Mate_Wiki_Comparsion = Dot(radius=1,color=BLUE_A).move_to([20,0,0]).shift(UP)
        Scipli_Wiki_Comparsion = Dot(radius=1.603,color=GOLD_B).move_to([25,0,0]).shift(UP*1.603)
        Enecune_Wiki_Comparsion = Dot(radius=1.468,color=YELLOW_A).move_to([30,0,0]).shift(UP*1.468)
        Fertumi_Wiki_Name = Text("Fertumi",font="NewComputerModern10").scale(10).next_to(Fertumi_Base_Wiki_Comparsion,UP,buff=2)
        Mate_Wiki_Name = Text("Mate",font="NewComputerModern10").next_to(Mate_Wiki_Comparsion,UP,buff=0.4)
        Scipli_Wiki_Name = Text("Scipli",font="NewComputerModern10").next_to(Scipli_Wiki_Comparsion,UP,buff=0.4)
        Enecune_Wiki_Name = Text("Enecune",font="NewComputerModern10").next_to(Enecune_Wiki_Comparsion,UP,buff=0.4)
        self.add(Fertumi_Wiki_Comparsion,Mate_Wiki_Comparsion,Scipli_Wiki_Comparsion,Enecune_Wiki_Comparsion,Fertumi_Wiki_Name)
        self.wait()
        self.play(self.camera.frame.animate.scale(1/5).move_to([25,6,0]))
        self.play(FadeOut(Fertumi_Wiki_Comparsion,Fertumi_Wiki_Name),FadeIn(Mate_Wiki_Name,Scipli_Wiki_Name,Enecune_Wiki_Name))
        self.play(self.camera.frame.animate.scale(1/4).move_to([18,1.5,0]),FadeOut(Mate_Wiki_Name,Scipli_Wiki_Name,Enecune_Wiki_Name))
        self.wait(0.5)
        Mate_Wiki = Text("Mate\nHot sub-jupiter\nSemi-Major Axis: 0.437 AU (65.375 M km)\nOrbital Period: 86.724 days\nEccentricity:0.026\nMass: 0.109 jupiter (34.643 earth)\nRadius: 0.6658 jupiter (7.463 earth or 47,544 km)\nTemperature: 473.22°C (746.37 K)\nStellar flux: 37.859x as earth",font="NewComputerModern10").move_to([16.4,1.5,0]).scale(0.25)
        Scipli_Wiki = Text("Scipli\nCool super-jupiter\nSemi-Major Axis: 2.905 AU (434.588 M km)\nOrbital Period: 4.07 years (1,486.41 days)\nEccentricity:0.027\nMass: 2.49 jupiter (788.21 earth)\nRadius: 1.0904 jupiter (11.965 earth or 76,232 km)\nTemperature: -46.62°C (226.53 K)\nStellar flux: 85.67% as earth",font="NewComputerModern10").move_to([19.5,0.8015*3,0]).scale(0.4)
        Enecune_Wiki = Text("Enecune\nFrozen jupiter\nSemi-Major Axis: 13.51 AU (2.0211 B km)\nOrbital Period: 40.84 years (14,907.42 days)\nEccentricity:0.057\nMass: 1.235 jupiter (392.51 earth)\nRadius: 0.9987 jupiter (10.959 earth or 69,822 km)\nTemperature: -168.11°C (105.04 K)\nStellar flux: 3.9612% as earth",font="NewComputerModern10").move_to([24.7,0.734*3,0]).scale(0.367)
        self.add(Mate_Wiki)
        self.wait(4)
        self.play(FadeOut(Mate_Wiki))
        self.play(self.camera.frame.animate.scale(1.603).move_to([22,0.8015*3,0]),Mate_Wiki_Comparsion.animate.shift(10*LEFT))
        self.wait(0.5)
        self.add(Scipli_Wiki)
        self.wait(4)
        self.play(FadeOut(Scipli_Wiki))
        self.play(self.camera.frame.animate.scale(0.91578).move_to([27,0.734*3,0]),Scipli_Wiki_Comparsion.animate.shift(10*LEFT))
        self.wait(0.5)
        self.add(Enecune_Wiki)
        self.wait(4)
        self.play(FadeOut(Enecune_Wiki))
        self.wait(0.5)

class PlanetSurface(ZoomedScene):
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        Fertumi_Base_View = Dot(radius=0.02192,color=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_Glow_View = create_glow(Fertumi_Base_View,rad=0.02192*80,col=ManimColor.from_rgb((255, 255, 252)))
        Fertumi_View = VGroup(Fertumi_Base_View,Fertumi_Glow_View).shift(3*RIGHT)
        Mate_Surface = Dot(radius=3,color=BLUE_A)
        planet_shadow = VGroup(Circle(radius=3,stroke_width=0,fill_color=BLACK,fill_opacity=0.7-idx/10).move_to(Mate_Surface).shift((3.5+idx/50)*LEFT) for idx in range(50))
        Scipli_Surface = Dot(radius=3,color=GOLD_B)
        Enecune_Surface = Dot(radius=3,color=YELLOW_A)
        self.add(Mate_Surface)
        self.wait(4)
        Mate_Surface.shift(3*LEFT)
        self.add(Fertumi_View,planet_shadow)
        self.wait(4)
        self.remove(Fertumi_View,planet_shadow,Mate_Surface)
        self.add(Scipli_Surface)
        self.wait(4)
        Scipli_Surface.shift(3*LEFT)
        Fertumi_View.scale(0.1504)
        self.add(Fertumi_View,planet_shadow)
        self.wait(4)
        self.remove(Fertumi_View,planet_shadow,Scipli_Surface)
        self.add(Enecune_Surface)
        self.wait(4)
        Enecune_Surface.shift(3*LEFT)
        Fertumi_View.scale(0.215)
        self.add(Fertumi_View,planet_shadow)
        self.wait(4)
        
class Temperature(Scene):
    def construct(self):
        Mate_Wiki_Comparsion = Dot(radius=1,color=BLUE_A).move_to([-5,0,0])
        Scipli_Wiki_Comparsion = Dot(radius=1.603,color=GOLD_B)
        Enecune_Wiki_Comparsion = Dot(radius=1.468,color=YELLOW_A).move_to([5,0,0])
        temperature = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_mate_c = Text("536.49°C",font="NewComputerModern10").next_to(Mate_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_scipli_c = Text("-29.66°C",font="NewComputerModern10").next_to(Scipli_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_enecune_c = Text("-155.81°C",font="NewComputerModern10").next_to(Enecune_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_mate_k = Text("809.61 K",font="NewComputerModern10").next_to(Mate_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_scipli_k = Text("243.49 K",font="NewComputerModern10").next_to(Scipli_Wiki_Comparsion,DOWN).scale(0.5)
        temperature_enecune_k = Text("117.34 K",font="NewComputerModern10").next_to(Enecune_Wiki_Comparsion,DOWN).scale(0.5)
        self.add(Mate_Wiki_Comparsion,Scipli_Wiki_Comparsion,Enecune_Wiki_Comparsion,temperature,temperature_mate_c,temperature_scipli_c,temperature_enecune_c)
        self.wait(5)
        self.play(Transform(temperature_mate_c,temperature_mate_k),Transform(temperature_scipli_c,temperature_scipli_k),Transform(temperature_enecune_c,temperature_enecune_k))
        self.wait(3)

class LateMainSequence(ZoomedScene):
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        Sol_comparsion = Dot(radius=1,fill_color=ManimColor.from_rgb((255, 242, 230)))
        Sol_comparsion_glow = create_glow(Sol_comparsion,rad=1*3,col=ManimColor.from_rgb((255, 242, 230)))
        Sol = VGroup(Sol_comparsion,Sol_comparsion_glow).shift(LEFT*3+UP)
        Fertumi_comparsion_late = Dot(radius=2.38,fill_color=ManimColor.from_rgb((255, 251, 245)))
        Fertumi_comparsion_late_glow = create_glow(Fertumi_comparsion_late,rad=2.38*3,col=ManimColor.from_rgb((255, 251, 245)))
        Fertumi_late = VGroup(Fertumi_comparsion_late,Fertumi_comparsion_late_glow).shift(RIGHT*3+UP*2.38)
        self.camera.frame.shift(3*UP)
        self.add(Fertumi_late,Sol)

## RED GIANT PHASE

class Pulse(Scene):
    def construct(self):
        def stellar_pulse(vmobject, rad=1, col=YELLOW_D): # stellar pulse
            glow_group = VGroup(Annulus(
                inner_radius=0.95*rad*(1.01**(idx)),
                outer_radius=1.05*rad*(1.01**(idx)), 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.05*np.sin(idx/60*PI/2)) for idx in range(60)).move_to(vmobject)
            return glow_group
        pulse_1 = stellar_pulse(ORIGIN,rad=0.5582)
        pulse_1.add_updater(lambda mob,dt: mob.scale(1.2))
        self.add(pulse_1)
        self.wait()

class Dialog_Box(Scene):
    def construct(self):
        ## HYDROGEN RUN OUT
        plane = NumberPlane().add_coordinates()
        round_rectangle = RoundedRectangle(corner_radius=0.1)
        chemistry = MathTex(r"^{1}{{H}}").set_color(BLUE_A).move_to([-1,0,0]).scale(2)  
        warning_triangle = Triangle().set_color(RED).scale(0.6)
        warning_sign = Text("!").set_color(RED).move_to(warning_triangle)
        warning = VGroup(warning_triangle,warning_sign).next_to(chemistry,buff=1)
        arrow_down = Polygram([[-1,-1,0],[-1.5,-2,0],[-1.7,-1,0]]).set_color(WHITE)   
        sq_info = Square(side_length=1.3).move_to([-6.4,-3.3,0])
        dialog_hydrogen_out = VGroup(round_rectangle,chemistry,warning,arrow_down).scale(0.5).move_to([-6,-1.5,0]) 
        ## HELIUM RUN OUT
        round_rectangle = RoundedRectangle(corner_radius=0.1)
        chemistry = MathTex(r"^{4}{{He}}").set_color(GREEN_C).move_to([-1,0,0]).scale(1.5)  
        warning_triangle = Triangle().set_color(RED).scale(0.6)
        warning_sign = Text("!").set_color(RED).move_to(warning_triangle)
        warning = VGroup(warning_triangle,warning_sign).next_to(chemistry,buff=1)
        arrow_down = Polygram([[-1,-1,0],[-1.5,-2,0],[-1.7,-1,0]]).set_color(WHITE)   
        sq_info = Square(side_length=1.3).move_to([-6.4,-3.3,0])
        dialog_helium_out = VGroup(round_rectangle,chemistry,warning,arrow_down).scale(0.5).move_to([-6,-1.5,0])
        self.add(sq_info,plane)
        self.add(dialog_hydrogen_out,arrow_down)
        self.wait()
        self.play(Transform(dialog_hydrogen_out,dialog_helium_out))

class ComparsionRedGiant(ZoomedScene):
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        Fertumi_comparsion = Dot(radius=12.1,fill_color=ManimColor.from_rgb((255, 221, 194)))
        Fertumi_comparsion_glow = create_glow(Fertumi_comparsion,rad=12.1*3,col=ManimColor.from_rgb((255, 221, 194)))
        Fertumi = VGroup(Fertumi_comparsion,Fertumi_comparsion_glow).shift(RIGHT*8+UP*12.1)
        Sol_comparsion = Dot(radius=1,fill_color=ManimColor.from_rgb((255, 242, 230)))
        Sol_comparsion_glow = create_glow(Sol_comparsion,rad=1*3,col=ManimColor.from_rgb((255, 242, 230)))
        Sol = VGroup(Sol_comparsion,Sol_comparsion_glow).shift(LEFT*9+UP)
        self.camera.frame.scale(4).shift(12*UP)
        Sol_text = Text("Sol",font="NewComputerModern10").next_to(Sol_comparsion,UP)
        Fertumi_text = Text("Fertumi",font="NewComputerModern10").next_to(Fertumi_comparsion,UP,buff=2).scale(3)
        self.add(Fertumi,Sol,Sol_text,Fertumi_text)

class TemperatureRedGiant(Scene):
    def construct(self):
        Scipli_RedGiant = Dot(radius=1.597,color=GOLD_B).move_to([-3,0,0])
        Enecune_RedGiant = Dot(radius=1.467,color=YELLOW_A).move_to([3,0,0])
        temperature_c = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_k = Text("Temperature in kelvin",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_scipli_c = Text("123.96°C",font="NewComputerModern10").next_to(Scipli_RedGiant,DOWN).scale(0.5)
        temperature_enecune_c = Text("-66.74°C",font="NewComputerModern10").next_to(Enecune_RedGiant,DOWN).scale(0.5)
        temperature_scipli_k = Text("397.11 K",font="NewComputerModern10").next_to(Scipli_RedGiant,DOWN).scale(0.5)
        temperature_enecune_k = Text("206.41 K",font="NewComputerModern10").next_to(Enecune_RedGiant,DOWN).scale(0.5)
        self.add(Scipli_RedGiant,Enecune_RedGiant,temperature_c,temperature_scipli_c,temperature_enecune_c)

## WHITE DWARF

class ComparsionWhiteDwarf(ZoomedScene):
    def construct(self):
        def create_glow(vmobject, rad=1, col=YELLOW): # Glow of star
            glow_group = VGroup(Circle(
                radius=rad*(1.002**(idx**2))/400, 
                stroke_opacity=0, 
                fill_color=col,
                fill_opacity=0.2-idx/300) for idx in range(60)).move_to(vmobject)
            return glow_group
        self.camera.frame.shift(3*UP)
        earth = SVGMobject("img\earth.svg").shift(UP+2*LEFT)
        Fertumi_white_dwarf_base = Dot(radius=1.429,fill_color=ManimColor.from_rgb((170, 198, 255)))
        Fertumi_white_dwarf_glow = create_glow(Fertumi_white_dwarf_base,rad=1.429*3,col=ManimColor.from_rgb((170, 198, 255)))
        Fertumi_white_dwarf = VGroup(Fertumi_white_dwarf_base,Fertumi_white_dwarf_glow).shift(1.429*UP+2*RIGHT)
        earth_text = Text("Earth",font="NewComputerModern10").next_to(earth,UP)
        fertumi_text = Text("Fertumi",font="NewComputerModern10").next_to(Fertumi_white_dwarf_base,UP)
        radius_note = MathTex(r"1.429 \ R_{E}").move_to([-6,6.5,0])
        self.add(earth,Fertumi_white_dwarf,earth_text,fertumi_text,radius_note)

class TemperatureAndMassWhiteDwarf(Scene):
    def construct(self):
        Scipli_WhiteDwarf = Dot(radius=1.594,color=GOLD_B).move_to([-3,0,0])
        Enecune_WhiteDwarf = Dot(radius=1.464,color=YELLOW_A).move_to([3,0,0])
        no_light_Scipli_WhiteDwarf = Dot(radius=1.594,fill_color=BLACK).move_to(Scipli_WhiteDwarf).set_opacity(0)
        no_light_Enecune_WhiteDwarf = Dot(radius=1.464,fill_color=BLACK).move_to(Enecune_WhiteDwarf).set_opacity(0.2)
        # Mass
        mass = Text("Mass",font="NewComputerModern10").to_edge(UP).scale(0.8)
        mass_scipli = MathTex(r"2.4885 \ M_{J}").next_to(Scipli_WhiteDwarf,DOWN).scale(0.7)
        mass_enecune = MathTex(r"1.2347 \ M_{J}").next_to(Enecune_WhiteDwarf,DOWN).scale(0.7)
        # Temperature
        temperature_c = Text("Temperature",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_k = Text("Temperature in kelvin",font="NewComputerModern10").to_edge(UP).scale(0.8)
        temperature_scipli_c = Text("-132.48°C",font="NewComputerModern10").next_to(Scipli_WhiteDwarf,DOWN).scale(0.5)
        temperature_enecune_c = Text("-154.79°C",font="NewComputerModern10").next_to(Enecune_WhiteDwarf,DOWN).scale(0.5)
        temperature_scipli_k = Text("140.67 K",font="NewComputerModern10").next_to(Scipli_WhiteDwarf,DOWN).scale(0.5)
        temperature_enecune_k = Text("118.36 K",font="NewComputerModern10").next_to(Enecune_WhiteDwarf,DOWN).scale(0.5)
        self.add(Scipli_WhiteDwarf,Enecune_WhiteDwarf,mass,mass_scipli,mass_enecune,no_light_Enecune_WhiteDwarf)  
        self.wait(3)
        self.play(ReplacementTransform(mass,temperature_c),ReplacementTransform(mass_scipli,temperature_scipli_c),ReplacementTransform(mass_enecune,temperature_enecune_c)) 
        self.wait(2)
        self.play(ReplacementTransform(temperature_c,temperature_k),ReplacementTransform(temperature_scipli_c,temperature_scipli_k),ReplacementTransform(temperature_enecune_c,temperature_enecune_k))
        self.wait(2)
