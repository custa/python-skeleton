import time
import tensorflow as tf


def export(export_dir):
    a = tf.constant(0.5)
    b = tf.constant(2.0)
    x = tf.placeholder(tf.float32, shape=[None, 1], name="Input-X")
    y = tf.add(tf.multiply(a, x), b, name="Output-Y")

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    builder = tf.saved_model.builder.SavedModelBuilder(export_dir)

    predict_signature_def = (
        tf.saved_model.signature_def_utils.predict_signature_def({"x": x}, {"y": y})
    )
    signature_def_map = {
        tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
        predict_signature_def
    }
    builder.add_meta_graph_and_variables(
        sess, [tf.saved_model.tag_constants.SERVING],
        signature_def_map=signature_def_map)
    builder.save()


if __name__ == "__main__":
    export("linear/{}".format(int(time.time())))
