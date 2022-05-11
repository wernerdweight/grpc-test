GRPC Test
====

This is just a small test to showcase the basics of gRPC.

The app itself is useless and only simulates a TV debate between two Czech presidents and a host. Therefore, everything is in the Czech language (not the code though).

Steps
---
1. You'll need `protoc` installed on your machine (and `go`, if you want to run this particular app - gRPC, however, supports many other languages).
2. Create a proto file in `ovm/ovm.proto` and write your service specification.
3. Download gRPC to be able to compile the proto file.
   ```shell
   # in repo root
   git clone https://github.com/grpc/grpc grpc
   cd grpc
   # init submodules (takes forever, but should happen during the clone above)
   git submodule update --init
   # prepare PHP and Python plugins (if you need to support those languages)
   mkdir -p cmake/build
   pushd cmake/build
   cmake ../..
   make protoc grpc_php_plugin
   make protoc grpc_python_plugin
   popd
   cd ..
   # generate client code and PB file
   protoc -I ovm/ ovm/ovm.proto --include_imports --include_source_info --descriptor_set_out=ovm/ovm.pb --go_out=plugins=grpc:ovm --php_out=plugins=grpc:ovm --grpc_out=ovm --plugin=protoc-gen-grpc=grpc/cmake/build/grpc_php_plugin --python_out=ovm --grpc_python_out=ovm --plugin=protoc-gen-grpc_python=grpc/cmake/build/grpc_python_plugin
   ```
4. Write your server and client code in `server.go` and `client.go`.
5. Run the server `go run server.go` and the client `go run client.go` (you can also compile them first if you want).
6. If your implementation is correct, you successfully finished and tested your first gRPC service.

Disclaimer
---
The replies that the server is returning when simulating the debate are in part real quotes of the politicians, in part adjusted versions, in part mostly made up.