#========[ IMPORTS ]========
from tests import *
import logging

# Setting up so that in the logs the file name shows up
#logger = logging.getLogger(__name__)

#========[ FUNCTIONS ]========

class Test_Main():
    def test_chamfer(self):
        test_chamfer.test_chamfer_distance()
        test_chamfer.test_dist_face()
        test_chamfer.test_divide()
        test_chamfer.test_norm()
        test_chamfer.test_Plan()
        test_chamfer.test_produit_scalaire()
        test_chamfer.test_produit_vectoriel()
        test_chamfer.test_vector()
    
    def test_classes(self):
        test_classes.test_Garment()
        test_classes.test_SMPLModel()
    
    def test_conversion(self):
        test_conversion.test_node_arc_incidence_matrix()
        test_conversion.test_numpyToVTK()
        test_conversion.test_toarray()
        test_conversion.test_toarray_without_loss()
        test_conversion.test_tofloat()
        test_conversion.test_tolist()
        test_conversion.test_trimesh_to_vtk()
    
    def test_neighbours(self):
        test_neighbours.test_nearest_neighbours_using_sklearn()
        test_neighbours.test_find()
        test_neighbours.test_get_nearest()
        test_neighbours.test_nearest_neighbours()
        test_neighbours.test_nearest_neighbours_generator()
    
    def test_nricp(self):
        test_nricp.test_non_rigid_icp()
        test_nricp.test_non_rigid_icp_generator()
        test_nricp.test_non_rigid_icp_generator_handler()
    
    def test_plot(self):
        test_plot.test_plot_alignment_multiple()
        test_plot.test_plot_alignment_single()
    
    def test_pretreat(self):
        test_pretreat.test_pretreating()
        test_pretreat.test_fillYZ()
        test_pretreat.test_replace()
    
    def test_rotation_translate(self):
        test_rotation_translate.test_axis_rotation()
        test_rotation_translate.test_origin_rotation()
    
    def test_solver(self):
        test_solver.test_spsolve()