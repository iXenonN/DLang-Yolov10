import std.stdio;
import std.socket;
import std.array;

void main() {
    auto address = new InternetAddress("127.0.0.1", 5000);
    auto client_socket = new TcpSocket();

    client_socket.connect(address);
    writeln("Connected to the Server!");

    while (true) {
        ulong message_size;

        // read message size
        if (client_socket.receive((cast(uint*)&message_size)[0..8]) == 0) {
            writeln("Disconnected.");
            break;
        }

        // error checking
        if (message_size == 0) {
            writeln("Invalid image size: ", message_size);
            continue; // invalid size continue loop
        }

        // get image
        auto buffer = new ubyte[message_size];
        if (client_socket.receive(buffer) == 0) {
            writeln("The connection to the server was lost.");
            break;
        }

        writeln("Image received, size: ", message_size);
    }
}

