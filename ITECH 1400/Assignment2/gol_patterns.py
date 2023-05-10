from numpy import zeros

pulsar_pattern = zeros((20, 20), dtype=int)
glider_pattern = zeros((20, 20), dtype=int)
toad_pattern = zeros((20, 20), dtype=int)
corners_block_pattern = zeros((20, 20), dtype=int)

#pulsar pattern
pulsar_pattern[2, 4] = 1
pulsar_pattern[2, 5] = 1
pulsar_pattern[2, 6] = 1
pulsar_pattern[2, 10] = 1
pulsar_pattern[2, 11] = 1
pulsar_pattern[2, 12] = 1
pulsar_pattern[4, 2] = 1
pulsar_pattern[4, 7] = 1
pulsar_pattern[4, 9] = 1
pulsar_pattern[4, 14] = 1
pulsar_pattern[5, 2] = 1
pulsar_pattern[5, 7] = 1
pulsar_pattern[5, 9] = 1
pulsar_pattern[5, 14] = 1
pulsar_pattern[6, 2] = 1
pulsar_pattern[6, 7] = 1
pulsar_pattern[6, 9] = 1
pulsar_pattern[6, 14] = 1
pulsar_pattern[7, 4] = 1
pulsar_pattern[7, 5] = 1
pulsar_pattern[7, 6] = 1
pulsar_pattern[7, 10] = 1
pulsar_pattern[7, 11] = 1
pulsar_pattern[7, 12] = 1
pulsar_pattern[9, 4] = 1
pulsar_pattern[9, 5] = 1
pulsar_pattern[9, 6] = 1
pulsar_pattern[9, 10] = 1
pulsar_pattern[9, 11] = 1
pulsar_pattern[9, 12] = 1
pulsar_pattern[10, 2] = 1
pulsar_pattern[10, 7] = 1
pulsar_pattern[10, 9] = 1
pulsar_pattern[10, 14] = 1
pulsar_pattern[11, 2] = 1
pulsar_pattern[11, 7] = 1
pulsar_pattern[11, 9] = 1
pulsar_pattern[11, 14] = 1
pulsar_pattern[12, 2] = 1
pulsar_pattern[12, 7] = 1
pulsar_pattern[12, 9] = 1
pulsar_pattern[12, 14] = 1
pulsar_pattern[14, 4] = 1
pulsar_pattern[14, 5] = 1
pulsar_pattern[14, 6] = 1
pulsar_pattern[14, 10] = 1
pulsar_pattern[14, 11] = 1
pulsar_pattern[14, 12] = 1


#glider pattern
glider_pattern[1, 3] = 1
glider_pattern[2, 1] = 1
glider_pattern[2, 3] = 1
glider_pattern[3, 2] = 1
glider_pattern[3, 3] = 1

#toad pattern
toad_pattern[1, 2] = 1
toad_pattern[1, 3] = 1
toad_pattern[1, 4] = 1
toad_pattern[2, 1] = 1
toad_pattern[2, 2] = 1
toad_pattern[2, 3] = 1

#corners block pattern
corners_block_pattern[0, 0] = 1
corners_block_pattern[0, 1] = 1
corners_block_pattern[1, 0] = 1
corners_block_pattern[1, 1] = 1
corners_block_pattern[2, 2] = 1
corners_block_pattern[0, 18] = 1
corners_block_pattern[0, 19] = 1
corners_block_pattern[1, 18] = 1
corners_block_pattern[1, 19] = 1
corners_block_pattern[2, 17] = 1
corners_block_pattern[18, 0] = 1
corners_block_pattern[18, 1] = 1
corners_block_pattern[17, 2] = 1
corners_block_pattern[19, 0] = 1
corners_block_pattern[19, 1] = 1
corners_block_pattern[17, 17] = 1
corners_block_pattern[18, 18] = 1
corners_block_pattern[18, 19] = 1
corners_block_pattern[19, 18] = 1
corners_block_pattern[19, 19] = 1

