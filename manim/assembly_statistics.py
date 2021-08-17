from manim import *
import numpy as np
from random import shuffle


'''An animation to illustrate assembly statistics such as N50, L50 and NG50'''

'''General flow:

- We can't presume a genome assembly is perfect.

- A genome assembly is complex - what part do we care about?

- For example, which of these two assemblies is 'better'?

- Completeness?  Fragmentation?

- Do we have a close reference genome? If not, hard to tell if we are missing anything.

- Compare two genomes, different fragmentation patterns. How do we assess these?

- The most common statistic for evaluating assmeblies is **N50**

- (animation showing N50)

- (show L50 from sorted contigs)

- (scale sorted contigs to genome size estimate, NG50)

- What about if we want to estimate the completeness of the genome?

'''

contig_lengths = [1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8]

class N50(Scene):
    def construct(self):
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contig_group = VGroup(*contigs)
        contig_group.shuffle()
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Total Length of all Contigs")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-4].set_color(YELLOW)
        self.play(Indicate(contig_group[-4]))
        b3 = Brace(contig_group[-4])
        b3_text = b3.get_text("N50")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(2)
        self.play(Indicate(b3_g))
        self.wait(5)


class N90(Scene):
    def construct(self):
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contig_group = VGroup(*contigs)
        contig_group.shuffle()
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Total Length of all Contigs")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"90\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=(contig_group.get_left() + contig_group.get_right() * 0.10), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-11].set_color(YELLOW)
        self.play(Indicate(contig_group[-11]))
        b3 = Brace(contig_group[-11])
        b3_text = b3.get_text("N90")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(2)
        self.play(Indicate(b3_g))
        self.wait(5)


class N50_90(Scene):
    def construct(self):
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contig_group = VGroup(*contigs)
        contig_group.shuffle()
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Total Length of all Contigs")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-4].set_color(YELLOW)
        self.play(Indicate(contig_group[-4]))
        b3 = Brace(contig_group[-4])
        b3_text = b3.get_text("N50")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(2)
        self.play(Indicate(b3_g))
        self.wait(5)
        self.play(FadeOut(b2_text), FadeOut(arrow))
        b2_text = Tex(r"90\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=(contig_group.get_left() + contig_group.get_right() * 0.10), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-11].set_color(YELLOW)
        self.play(Indicate(contig_group[-11]))
        b3 = Brace(contig_group[-11])
        b3_text = b3.get_text("N90")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.wait(2)
        self.play(Indicate(b3_g))
        self.wait(5)




class L50(Scene):
    def construct(self):
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contig_group = VGroup(*contigs)
        contig_group.shuffle()
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Total Length of all Contigs")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-4:].set_color(YELLOW)
        self.play(Indicate(contig_group[-4:]))
        b3 = Brace(contig_group[-4:])
        b3_text = b3.get_text("L50 = Number of contigs = 4")
        b3_g = VGroup(b3, b3_text)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(2)
        b3_g.set_color(YELLOW)
        self.play(Indicate(b3_g))
        self.wait(5)


class NG50(Scene):
    def construct(self):
        contig_lengths = [1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8]
        shuffle(contig_lengths)
        # Add an extra contig length here, we'll make it invisible. This is the 'extra' space left in the genome.
        contig_lengths.insert(0, 18)
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contigs[0].set_opacity(0)
        contig_group = VGroup(*contigs)
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        # Move empty space to start of list again.
        contigs.insert(0, contigs.pop())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Estimated Genome Size")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Estimated Genome Size").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-6].set_color(YELLOW)
        self.play(Indicate(contig_group[-6]))
        b3 = Brace(contig_group[-6])
        b3_text = b3.get_text("NG50")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(1)
        self.play(Indicate(b3_g))
        self.wait(5)


class AssemblyStatistics(Scene):
    def construct(self):
        self.n50_90_intro()
        self.fadeOutAll()
        self.n50_90()
        self.fadeOutAll()
        self.l50_intro()
        self.fadeOutAll()
        self.l50()
        self.fadeOutAll()
        self.ng50_intro()
        self.fadeOutAll()
        self.ng50()
        self.fadeOutAll()
    
    def n50_90_intro(self):
        intro_text = Text("N50 and N90 statistics")
        self.play(FadeIn(intro_text))
        self.wait(5)

    def ng50_intro(self):
        intro_text = Text("NG50 statistic")
        self.play(FadeIn(intro_text))
        self.wait(5)

    def l50_intro(self):
        intro_text = Text("L50 statistic")
        self.play(FadeIn(intro_text))
        self.wait(5)

    def ng50(self):
        contig_lengths = [1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8]
        shuffle(contig_lengths)
        # Add an extra contig length here, we'll make it invisible. This is the 'extra' space left in the genome.
        contig_lengths.insert(0, 18)
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contigs[0].set_opacity(0)
        contig_group = VGroup(*contigs)
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        s1_text = Text("Sort contigs by length").scale(0.8).to_corner(UL)
        self.play(FadeIn(s1_text))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        # Move empty space to start of list again.
        contigs.insert(0, contigs.pop())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        self.play(FadeOut(s1_text))
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Estimated Genome Size")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Estimated Genome Size").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-6].set_color(YELLOW)
        self.play(Indicate(contig_group[-6]))
        b3 = Brace(contig_group[-6])
        b3_text = b3.get_text("NG50")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(1)
        self.play(Indicate(b3_g))
        self.wait(10)

    def l50(self):
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contig_group = VGroup(*contigs)
        contig_group.shuffle()
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        s1_text = Text("Sort contigs by length").scale(0.8).to_corner(UL)
        self.play(FadeIn(s1_text))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        self.play(FadeOut(s1_text))
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Total Length of all Contigs")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-4:].set_color(YELLOW)
        self.play(Indicate(contig_group[-4:]))
        b3 = Brace(contig_group[-4:])
        b3_text = b3.get_text("L50 = Number of contigs = 4")
        b3_g = VGroup(b3, b3_text)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(2)
        b3_g.set_color(YELLOW)
        self.play(Indicate(b3_g))
        self.wait(10)

    def n50_90(self):
        contigs = [Rectangle(width=x) for x in contig_lengths]
        contig_group = VGroup(*contigs)
        contig_group.shuffle()
        contig_group.arrange(buff=1)
        contig_group.scale_to_fit_width(12)
        self.play(FadeIn(contig_group))
        self.wait(2)
        s1_text = Text("Sort contigs by length").scale(0.8).to_corner(UL)
        self.play(FadeIn(s1_text))
        self.wait(2)
        contigs.sort(key=lambda x: x.get_width())
        contig_group = VGroup(*contigs)
        self.play(contig_group.animate().arrange().scale_to_fit_width(12))
        self.wait(2)
        self.play(FadeOut(s1_text))
        b1 = Brace(contig_group)
        b1_text = b1.get_text("Total Length of all Contigs")
        self.play(FadeIn(b1), FadeIn(b1_text))
        b2_text = Tex(r"50\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=contig_group.get_center(), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-4].set_color(YELLOW)
        self.play(Indicate(contig_group[-4]))
        b3 = Brace(contig_group[-4])
        b3_text = b3.get_text("N50")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.play(VGroup(b1, b1_text).animate().to_edge(DOWN))
        self.wait(2)
        self.play(Indicate(b3_g))
        self.wait(5)
        self.play(FadeOut(b2_text), FadeOut(arrow))
        b2_text = Tex(r"90\% of Total Length").scale(0.8)
        arrow = Arrow(start=contig_group.get_right(), end=(contig_group.get_left() + contig_group.get_right() * 0.10), color=WHITE, buff=0).next_to(contig_group, UP, aligned_edge=RIGHT)
        b2_text.next_to(arrow, UP)
        self.play(Create(arrow), FadeIn(b2_text))
        self.wait(2)
        contig_group[-11].set_color(YELLOW)
        self.play(Indicate(contig_group[-11]))
        b3 = Brace(contig_group[-11])
        b3_text = b3.get_text("N90")
        b3_g = VGroup(b3, b3_text)
        b3_g.set_color(YELLOW)
        self.wait(2)
        self.play(Indicate(b3_g))
        self.wait(10)

    def fadeOutAll(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
 