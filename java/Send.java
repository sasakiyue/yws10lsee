import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Send {
  private final static String QUEUE_NAME = "hello";

  public static void main(String[] argv) throws Exception {

    ConnectionFactory factory = new ConnectionFactory();

    factory.setHost("rabbit");
    Connection connection = factory.newConnection();
    Channel channel = connection.createChannel();

    channel.queueDeclare(QUEUE_NAME, false, false, false, null); //3.queue宣言
    String message = "Hello World!";                             //4.messageのpublish
    channel.basicPublish("", QUEUE_NAME, null, message.getBytes("UTF-8"));//4.messageのpublish
    System.out.println(" [x] Sent '" + message + "'");

    channel.close(); //5.Channel閉じる
    connection.close(); //6.Connection閉じる
    # build test
  }
}
