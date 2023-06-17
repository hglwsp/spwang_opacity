import torch
import prob
import superp
import sample
import sample_u
import sample_d


############################################
# generating training data set
############################################

def gen_batch_data():
    ##########################################
    # get x1,x2,x3,x4 full_Data
    ##########################################
    def gen_full_data(region, len_sample):
        grid_sample = [torch.linspace(region[i][0], region[i][1], int(len_sample[i])) for i in range(superp.DIM_S)] # gridding each dimension
        mesh = torch.meshgrid(grid_sample) # mesh the gridding of each dimension
        flatten = [torch.flatten(mesh[i]) for i in range(len(mesh))] # flatten the list of meshes
        nn_input = torch.stack(flatten, 1) # stack the list of flattened meshes
        return nn_input
    full_init = gen_full_data(prob.INIT, superp.DATA_LEN_I)
    full_unsafe_1 = gen_full_data(prob.UNSAFE_1, superp.DATA_LEN_U1)
    full_unsafe_2 = gen_full_data(prob.UNSAFE_2, superp.DATA_LEN_U2)
    full_domain = gen_full_data(prob.DOMAIN, superp.DATA_LEN_D)

    def batch_data(full_data, data_length, data_chunks, filter):
        l = list(data_length)
        batch_list = [torch.reshape(full_data, l + [superp.DIM_S])]
        for i in range(superp.DIM_S):
            batch_list = [tensor_block for curr_tensor in batch_list for tensor_block in list(curr_tensor.chunk(int(data_chunks[i]), i))]
        
        batch_list = [torch.reshape(curr_tensor, [-1, superp.DIM_S]) for curr_tensor in batch_list]
        batch_list = [curr_tensor[filter(curr_tensor)] for curr_tensor in batch_list]
        batch_list = [curr_tensor for curr_tensor in batch_list if len(curr_tensor) > 0]

        return batch_list

    batch_init = batch_data(full_init, superp.DATA_LEN_I, superp.BLOCK_LEN_I, prob.cons_init)
    batch_init.append(torch.tensor([[0.0,1.0,0.0,0.0]
    ]))
    batch_unsafe_1 = batch_data(full_unsafe_1, superp.DATA_LEN_U1, superp.BLOCK_LEN_U1, prob.cons_unsafe)
    batch_unsafe_2 = batch_data(full_unsafe_2, superp.DATA_LEN_U2, superp.BLOCK_LEN_U2, prob.cons_unsafe)
    # batch_unsafe_1.append(torch.tensor([[3.798945054612738e-12, 1.010000000003799, 0.0, 0.1]]))
    # batch_unsafe_1.append(torch.tensor([[1.005, 0.0, 0.1, 0.0]]))
    # batch_unsafe_1.append(torch.tensor([[0.0, 1.002999999996818, 0.0, 0.1]]))
    # batch_unsafe.append(sample_u.sam)
    batch_domain = batch_data(full_domain, superp.DATA_LEN_D, superp.BLOCK_LEN_D, prob.cons_domain)
    # batch_domain.append(torch.tensor([[0.014484766746720102, 1.4127046087845967, 0.0, 0.1]]))
    # batch_domain.append(sample_d.sample)

    return batch_init, batch_unsafe_1, batch_unsafe_2,batch_domain
