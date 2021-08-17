from manim import *
import numpy as np

kmer_size = 4
sequence = "AAAGGCGTTGAGGTTT"
kmers = [sequence[i: i+kmer_size] for i in range(len(sequence) - kmer_size + 1)]
reads = [sequence[3*i:3*i+6] for i in range(len(sequence) // 3)]

kmer_edges = []
for i, kmer in enumerate(kmers):
    for j, kmer_2 in enumerate(kmers):
        if kmer[1:] == kmer_2[0:-1]:
            kmer_edges.append((i,j))

kmer_dict = {i:Text(kmer, color=BLACK, size=0.4, font="Consolas") for i, kmer in enumerate(kmers)}

hamiltonian_layout = {
    0: (-6, 0, 0),
    1: (-4, 0, 0),
    2: (-2.5, -1, 0),
    3: (-1, -3, 0),
    4: (1, -3, 0),
    5: (2.5, -1, 0),
    6: (2.5, 1, 0),
    7: (1, 3, 0),
    8: (-1, 3, 0),
    9: (-2.5, 1, 0),
    10: (-1, 0, 0),
    11: (1, 0, 0),
    12: (4, 0, 0)
}

eulerian_layout = {
    0: (-6, 0, 0),
    1: (-4, 0, 0),
    2: (-2, 0, 0),
    3: (-1.5, -1.5, 0),
    4: (0, -2, 0),
    5: (1.5, -1.5, 0),
    6: (2, 0, 0),
    7: (1.5, 1.5, 0),
    8: (0, 2, 0),
    9: (-1.5, 1.5, 0),
    10: (0, 0, 0),
    11: (4, 0, 0)
}

paths_through_hamiltonian = [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                             (0, 1, 10, 11, 6, 7, 8, 9, 2, 3, 4, 5, 12)]

paths_xyz_through_hamiltonian = [(hamiltonian_layout[x] for x in y) for y in paths_through_hamiltonian]


paths_through_eulerian = [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 10, 6, 11),
                             (0, 1, 2, 10, 6, 7, 8, 9, 2, 3, 4, 5, 6, 11)]

paths_xyz_through_eulerian = [(eulerian_layout[x] for x in y) for y in paths_through_eulerian]
# Bit of a hack to make the path distinguishable
paths_xyz_through_eulerian[0] = ((x[0], x[1] + (i - 5) / 15, x[2]) for i, x in enumerate(paths_xyz_through_eulerian[0]))
paths_xyz_through_eulerian[1] = ((x[0], x[1] - (i - 5) / 15, x[2]) for i, x in enumerate(paths_xyz_through_eulerian[1]))
eulerian_edges = [
    (0,1),
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (5,6),
    (6,7),
    (7,8),
    (8,9),
    (9,2),
    (2,10),
    (10,6),
    (6,11)
]

eulerian_node_label_text = {
    0: "AAA",
    1: "AAG",
    2: "AGG",
    3: "GGC",
    4: "GCG",
    5: "CGT",
    6: "GTT",
    7: "TTG",
    8: "TGA",
    9: "GAG",
    10: "GGT",
    11: "TTT"
}

eulerian_node_labels = {key: Text(value, color=BLACK, size=0.4, font="Consolas") for key, value in eulerian_node_label_text.items()}


class TestHLayout(Scene):
    def construct(self):
        vertices = list(range(len(kmers)))
        edges = kmer_edges
        g = Graph(vertices, edges, layout=hamiltonian_layout,
                  labels=kmer_dict, edge_config={'buff': 0.35}, edge_type=Arrow)
        self.add(g)
        print(g.__dict__)

class TestELayout(Scene):
    def construct(self):
        vertices = eulerian_layout.keys()
        edges = eulerian_edges
        g = Graph(vertices, edges, layout=eulerian_layout,
                  edge_config={'buff': 0.35}, vertex_type=Circle,
                  vertex_config={'radius': 0.3, 'color': WHITE}, edge_type=Arrow)
        self.add(g)

class TestELayoutLabeled(Scene):
    def construct(self):
        vertices = eulerian_layout.keys()
        edges = eulerian_edges
        g = Graph(vertices, edges, layout=eulerian_layout,
                  edge_config={'buff': 0.35, "stroke_opacity": 0.4, "tip_length": 0.13}, labels=eulerian_node_labels, edge_type=Arrow)
        self.add(g)
        for edge_key, edge in g.edges.items():
            edge_label = eulerian_node_labels[edge_key[0]].original_text + eulerian_node_labels[edge_key[1]].original_text[-1]
            print(edge_label)
            edge_label_text = Text(edge_label, color=WHITE, size=0.4, font="Consolas")
            edge_label_text.move_to(edge, aligned_edge=ORIGIN)
            angle = edge.get_angle()
            if abs(angle) > (PI / 2):
                angle = angle - PI
            edge_label_text.rotate(angle)
            #edge.set_opacity(0.4)
            self.add(edge_label_text)



class KmerGen(Scene):
    def construct(self):
        scene_heading = Text("De Novo Genome Assembly:", font="Noto Sans")
        scene_subheading = Text("de Bruijn Graphs", font="Noto Sans", color=RED)
        scene_subheading.next_to(scene_heading, direction=DOWN)
        self.play(Write(scene_heading))
        self.play(Write(scene_subheading))
        self.wait(4)
        self.play(Unwrite(scene_heading), Unwrite(scene_subheading))
        self.wait(2)
        vertices = list(range(len(kmers)))
        edges = kmer_edges
        g = Graph(vertices, edges, layout=hamiltonian_layout,
                  labels=kmer_dict, edge_config={'buff': 0.35}, edge_type=Arrow)
        seq = Text(sequence, color=WHITE, font="Consolas")
        kmer_list = []
        for kmer in kmers:
            kmer_list.append(Text(kmer, color=WHITE, font="Consolas"))
        seq.to_edge(UP)
        self.play(Write(seq))
        self.wait(10)
        kmer_gen_text = Text("Generate Kmers (k=4)", font="Noto Sans", size=0.6, color=GREEN)
        kmer_gen_text.to_edge(LEFT)
        self.play(FadeIn(kmer_gen_text))
        self.wait(1)
        for i, kmer in enumerate(kmer_list):
            kmer.to_edge(UP)
            kmer.align_to(seq[i], LEFT)
            self.play(kmer.animate.shift(DOWN * (i+1) * 0.5), run_time=0.3)
        self.wait(2)
        self.play(FadeOut(seq))
        kmer_group = Group(*kmer_list)
        self.play(kmer_group.animate.arrange(direction=DOWN, aligned_edge=LEFT).scale_in_place(0.7).next_to(RIGHT * 5.5))
        self.wait(2)
        self.play(FadeOut(kmer_gen_text))
        challenge_text = Text("Challenge: Reassemble original sequence", font="Noto Sans",
                                    size=0.8, t2w={'Challenge:': BOLD})
        challenge_text_followup = Text("Remember we don't know the order of Kmers...", font="Noto Sans",
                                    size=0.6)
        challenge_text_followup_2 = Text('For short read assembly, use a de Bruijn graph', font="Noto Sans",
                                    size=0.6, t2c={"de Bruijn": RED}, disable_ligatures=True)
        print(challenge_text_followup_2.original_text)
        challenge_text_followup.next_to(challenge_text, DOWN)
        challenge_text_followup_2.next_to(challenge_text_followup, DOWN)
        self.play(FadeIn(challenge_text))
        self.play(FadeIn(challenge_text_followup))
        self.wait(5)
        self.play(FadeIn(challenge_text_followup_2))
        self.wait(10)
        self.play(FadeOut(challenge_text), FadeOut(challenge_text_followup), FadeOut(challenge_text_followup_2))
        hamiltonian_heading = Text("Hamiltonian\nde Bruijn graph", font="Noto Sans",
                                    size=0.8)
        hamiltonian_heading.to_corner(UL)
        self.play(FadeIn(hamiltonian_heading))
        self.wait(5)

        kmer_exp_1 = Text("• For any given kmer, get the (k-1)-mer suffix", font="Noto Sans",
                                    size=0.7, t2s={"(k-1)": ITALIC}, t2c={'suffix': YELLOW}, disable_ligatures=True)
        kmer_exp_2 = Text("• Find all kmers with matching (k-1)-mer prefix", font="Noto Sans",
                                    size=0.7, t2s={"(k-1)": ITALIC}, t2c={'prefix': RED}, disable_ligatures=True)
        kmer_exp_3 = Text("• Repeat for all kmers", font="Noto Sans",
                                    size=0.7)
        kmer_exp_1.to_edge(LEFT)
        kmer_exp_2.next_to(kmer_exp_1, DOWN, aligned_edge=LEFT)
        kmer_exp_3.next_to(kmer_exp_2, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(kmer_exp_1))
        self.wait(5)
        self.play(FadeIn(kmer_exp_2))
        self.wait(5)
        self.play(FadeIn(kmer_exp_3))
        self.wait(5)

        node_exp_text = Text("Nodes: Kmers", font="Noto Sans",
                                    size=0.5, t2w={'Nodes:': BOLD}, t2c={'Nodes:': BLUE})
        edge_exp_text = Text("Edges: Kmer overlap", font="Noto Sans",
                                    size=0.5, t2w={'Edges:': BOLD}, t2c={'Edges:': BLUE})
        node_exp_text.move_to((2, 3, 0), aligned_edge=LEFT)
        edge_exp_text.next_to(node_exp_text, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(node_exp_text), FadeIn(edge_exp_text))

        self.wait(5)
        self.play(FadeOut(VGroup(kmer_exp_1, kmer_exp_2, kmer_exp_3)))
        for kmer in kmer_group[0:-1]:     # Don't need to highlight last kmer
            self.highlight_next_kmers(kmer, kmer_group)
            self.introduce_graph_node(g, kmer)
            self.play(kmer_group.animate.set_color(WHITE))
        self.wait(10)
        hpath_explanation = Text("Hamiltonian path:\nA path that visits each\nnode exactly once", font="Noto Sans",
                                    size=0.6, t2w={'Hamiltonian path:': BOLD}, color=GREEN)
        hpath_explanation.to_corner(DL)
        self.play(FadeIn(hpath_explanation))
        self.wait(2)
        path_1 = VMobject(stroke_opacity=0.6, stroke_color=YELLOW, stroke_width=20)
        path_1.set_points_smoothly([*paths_xyz_through_hamiltonian[0]])
        self.play(Create(path_1), run_time=5)
        self.wait(8)
        self.play(FadeOut(path_1))

        path_2 = VMobject(stroke_opacity=0.6, stroke_color=YELLOW, stroke_width=20)
        path_2.set_points_smoothly([*paths_xyz_through_hamiltonian[1]])
        self.play(Create(path_2), run_time=5)
        self.wait(8)
        self.play(FadeOut(path_2))
        self.wait(2)

        self.play(FadeOut(g))
        self.play(FadeOut(VGroup(hpath_explanation, hamiltonian_heading)), FadeOut(node_exp_text), FadeOut(edge_exp_text))
        self.wait(3)

        eulerian_heading = Text("Eulerian\nde Bruijn graph", font="Noto Sans",
                                    size=0.8)
        eulerian_heading.to_corner(UL)
        self.play(FadeIn(eulerian_heading))
        self.wait(8)
        kmer_exp_1 = Text("• For any given kmer, add the suffix and \n   prefix (k-1)-mers as graph nodes \n   (if not already present)", font="Noto Sans",
                                    size=0.7, t2s={"(k-1)": ITALIC}, t2c={'suffix': YELLOW, 'prefix': RED}, disable_ligatures=True)
        kmer_exp_2 = Text("• Add edge connecting suffix and prefix (k-1)-mers", font="Noto Sans",
                                    size=0.7, t2s={"(k-1)": ITALIC}, t2c={'suffix': YELLOW, 'prefix': RED}, disable_ligatures=True)
        kmer_exp_3 = Text("• Repeat for all kmers", font="Noto Sans",
                                    size=0.7)
        kmer_exp_1.to_edge(LEFT)
        kmer_exp_2.next_to(kmer_exp_1, DOWN, aligned_edge=LEFT)
        kmer_exp_3.next_to(kmer_exp_2, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(kmer_exp_1))
        self.wait(8)
        self.play(FadeIn(kmer_exp_2))
        self.wait(8)
        self.play(FadeIn(kmer_exp_3))
        self.wait(6)


        node_exp_text = Text("Nodes: Kmer suffix/prefix", font="Noto Sans",
                                    size=0.5, t2w={'Nodes:': BOLD}, t2c={'Nodes:': BLUE, "suffix": YELLOW, "prefix": RED}, disable_ligatures=True)
        edge_exp_text = Text("Edges: Kmers", font="Noto Sans",
                                    size=0.5, t2w={'Edges:': BOLD}, t2c={'Edges:': BLUE, 'Kmers': GREEN}, disable_ligatures=True)
        node_exp_text.move_to((1, 3, 0), aligned_edge=LEFT)
        edge_exp_text.next_to(node_exp_text, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(node_exp_text), FadeIn(edge_exp_text))
        self.wait(5)
        self.play(FadeOut(VGroup(kmer_exp_1, kmer_exp_2, kmer_exp_3)))

        g_eur, edge_labels_eur = self.make_eulerian_graph(eulerian_node_label_text.keys(),
                                                          eulerian_edges, eulerian_layout,
                                                          eulerian_node_labels)
        for kmer in kmer_group:
            self.highlight_kmer(kmer, GREEN, indicate=True)
            self.introduce_kmer_text(edge_labels_eur, kmer)
            self.highlight_prefix_suffix_nodes(g_eur, kmer)
            self.play(kmer_group.animate.set_color(WHITE))
        self.wait(10)
        epath_explanation = Text("Eulerian path:\nA path that visits each\nedge exactly once", font="Noto Sans",
                                    size=0.6, t2w={'Eulerian path:': BOLD}, color=GREEN, disable_ligatures=True)
        epath_explanation.to_corner(DL)
        self.play(FadeIn(epath_explanation))
        self.wait(2)
        path_1 = VMobject(stroke_opacity=0.6, stroke_color=YELLOW, stroke_width=20)
        path_1.set_points_smoothly([*paths_xyz_through_eulerian[0]])
        self.play(Create(path_1), run_time=5)
        self.wait(8)
        self.play(FadeOut(path_1))

        path_2 = VMobject(stroke_opacity=0.6, stroke_color=YELLOW, stroke_width=20)
        path_2.set_points_smoothly([*paths_xyz_through_eulerian[1]])
        self.play(Create(path_2), run_time=5)
        self.wait(12)
        self.play(FadeOut(path_2))
        self.wait(2)

        self.play(FadeOut(g_eur), FadeOut(VGroup(*list(edge_labels_eur.values()))))
        self.play(FadeOut(VGroup(epath_explanation, eulerian_heading)), FadeOut(node_exp_text), FadeOut(edge_exp_text), FadeOut(VGroup(*kmer_list)))
        self.wait(3)

        #TODO Contig explanation - removal of nodes/edges in respective graphs.

    def make_eulerian_graph(self, vertices, edges, layout, labels):
        g = Graph(vertices, edges, layout=layout,
                  edge_config={'buff': 0.35, "stroke_opacity": 0.4, "tip_length": 0.13}, labels=labels, edge_type=Arrow)
        edge_label_text_dict = {}
        for edge_key, edge in g.edges.items():
            edge_label = labels[edge_key[0]].original_text + labels[edge_key[1]].original_text[-1]
            edge_label_text = Text(edge_label, color=GREEN, size=0.4, font="Consolas")
            edge_label_text.move_to(edge, aligned_edge=ORIGIN)
            angle = edge.get_angle()
            if abs(angle) > (PI / 2):
                angle = angle - PI
            edge_label_text.rotate(angle)
            edge_label_text_dict[edge_key] = edge_label_text
        return g, edge_label_text_dict

    def highlight_next_kmers(self, kmer, kmer_group):
        self.play(kmer[1:].animate.set_color(YELLOW), run_time=0.5)
        self.play(Indicate(kmer[1:], color=None))
        kmer_text = kmer.original_text
        suffix = kmer_text[1:]
        for comp_kmer in kmer_group:
            if kmer is comp_kmer:
                continue
            prefix = comp_kmer.original_text[0:-1]
            if suffix == prefix:
                self.play(comp_kmer[0:-1].animate.set_color(RED), run_time=0.5)
                self.play(Indicate(comp_kmer[0:-1], color=None))
        
    def highlight_kmer(self, kmer, color=RED, indicate=False):
        self.play(kmer.animate.set_color(color), run_time=0.5)
        if indicate:
            self.play(Indicate(kmer, color=None))
        return

    def highlight_prefix_suffix_nodes(self, g, kmer):
        prefix = kmer.original_text[0:-1]
        suffix = kmer.original_text[1:]
        for key, node in g.vertices.items():
            label = g._labels[key].original_text
            if prefix == label:
                prefix_key = key
            if suffix == label:
                suffix_key = key
        self.play(Indicate(g.vertices[prefix_key], color=YELLOW), 
                  Indicate(g.vertices[suffix_key], color=RED),
                  Create(g.edges[(prefix_key, suffix_key)]))
        return

    def introduce_kmer_text(self, edge_labels, kmer):
        for label in edge_labels.values():
            if label.original_text == kmer.original_text:
                self.play(FadeIn(label))

    def introduce_graph_node(self, g, kmer):
        for key, node in g.vertices.items():
            label = g._labels[key].original_text
            if kmer.original_text == label:
                self.play(Indicate(node, color=YELLOW), run_time=0.6)
                start_key = key
        for key, node in g.vertices.items():
            label = g._labels[key].original_text
            if kmer.original_text[1:] == label[0:-1]:
                self.play(Create(g.edges[(start_key, key)], run_time=0.5))
                self.play(Indicate(node, color=RED), run_time=0.6)

