logout.pb.o: logout.pb.cc logout.pb.h
 g++  -O3 -Werror -MMD -ggdb -pipe -D_GNU_SOURCE  -c -I/data/edifierli/svr_proj/trunk/src/../ext/tsf4g_base_2_1_13853_64/include  -I/data/edifierli/svr_proj/trunk/src/../snslib -I/data/edifierli/svr_proj/trunk/src/../ext/snsapp/v1 -I/usr/local/include/google/protobuf -I/data/edifierli/svr_proj/trunk/src/../ext/rapidxml-1.13 -I/data/edifierli/svr_proj/trunk/src/proto -I/data/edifierli/svr_proj/trunk/src/../ext/xml_parser -I/data/edifierli/svr_proj/trunk/src/../ext/uds_api_2 -I /data/edifierli/svr_proj/trunk/src/../ext -I/data/edifierli/svr_proj/trunk/src/include -I/data/edifierli/svr_proj/trunk/src/../ext/MGW_API_V2.0R090_suse_x86_64/inc -I/data/edifierli/svr_proj/trunk/src/../ext/MsgPlatform_API_V1.1R020-SUSE-64bit-with-fpic/include logout.pb.cc -o logout.pb.o
